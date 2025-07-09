"""
템플릿 관리 (Template Management)
"""
import os
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

from ..config import settings
from ..config.constants import (
    TEMPLATE_CATEGORIES, DEVELOPMENT_LANGUAGES, DEVELOPMENT_FRAMEWORKS,
    CONTENT_TYPES, CONTENT_PLATFORMS, LEARNING_TYPES, CACHE_UPDATE_INTERVAL
)
from ..utils import (
    print_info, print_error, print_warning, show_progress,
    is_git_available, clone_repository, update_repository, get_remote_tags,
    clone_specific_tag, get_repository_info, safe_remove
)


class TemplateManager:
    """템플릿 관리자 클래스"""
    
    def __init__(self):
        self.cache_dir = settings.get_cache_dir()
        self.templates_dir = self.cache_dir / "templates"
        self.repo_url = settings.get_repo_url()
        self.branch = settings.get_branch()
        
        # 캐시 디렉토리 생성
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def ensure_cache_updated(self, force: bool = False) -> bool:
        """캐시가 최신 상태인지 확인하고 필요시 업데이트"""
        if not is_git_available():
            print_error("Git이 설치되지 않았습니다. Git을 설치해주세요.")
            return False
        
        cache_info_file = self.cache_dir / "cache_info.json"
        needs_update = force
        
        if not needs_update and cache_info_file.exists():
            try:
                import json
                with open(cache_info_file, 'r') as f:
                    cache_info = json.load(f)
                
                last_update = datetime.fromisoformat(cache_info.get('last_update', '1970-01-01'))
                if datetime.now() - last_update > timedelta(seconds=CACHE_UPDATE_INTERVAL):
                    needs_update = True
                    
            except (json.JSONDecodeError, ValueError):
                needs_update = True
        else:
            needs_update = True
        
        if needs_update:
            return self._update_cache()
        
        return True
    
    def _update_cache(self) -> bool:
        """캐시 업데이트"""
        print_info("템플릿 캐시 업데이트 중...")
        
        # 저장소 클론/업데이트
        if self.templates_dir.exists():
            success = update_repository(self.templates_dir, self.repo_url, self.branch)
        else:
            success = clone_repository(self.repo_url, self.templates_dir, self.branch)
        
        if success:
            # 캐시 정보 업데이트
            cache_info = {
                "last_update": datetime.now().isoformat(),
                "repo_url": self.repo_url,
                "branch": self.branch
            }
            
            import json
            cache_info_file = self.cache_dir / "cache_info.json"
            with open(cache_info_file, 'w') as f:
                json.dump(cache_info, f, indent=2)
            
            print_info("템플릿 캐시 업데이트 완료")
            return True
        
        return False
    
    def get_available_templates(self) -> Dict[str, List[str]]:
        """사용 가능한 템플릿 목록 반환"""
        if not self.ensure_cache_updated():
            return {}
        
        templates = {
            "development": [],
            "content": [],
            "learning": []
        }
        
        templates_root = self.templates_dir / "templates"
        
        if not templates_root.exists():
            return templates
        
        # 개발 템플릿
        dev_dir = templates_root / "development"
        if dev_dir.exists():
            templates["development"] = self._scan_development_templates(dev_dir)
        
        # 콘텐츠 템플릿
        content_dir = templates_root / "content"
        if content_dir.exists():
            templates["content"] = self._scan_content_templates(content_dir)
        
        # 학습 템플릿
        learning_dir = templates_root / "learning"
        if learning_dir.exists():
            templates["learning"] = self._scan_learning_templates(learning_dir)
        
        return templates
    
    def _scan_development_templates(self, dev_dir: Path) -> List[str]:
        """개발 템플릿 스캔"""
        templates = []
        
        for lang_dir in dev_dir.iterdir():
            if not lang_dir.is_dir() or lang_dir.name.startswith('.'):
                continue
                
            for framework_dir in lang_dir.iterdir():
                if not framework_dir.is_dir() or framework_dir.name.startswith('.'):
                    continue
                
                template_path = f"development/{lang_dir.name}/{framework_dir.name}"
                templates.append(template_path)
        
        return templates
    
    def _scan_content_templates(self, content_dir: Path) -> List[str]:
        """콘텐츠 템플릿 스캔"""
        templates = []
        
        for type_dir in content_dir.iterdir():
            if not type_dir.is_dir() or type_dir.name.startswith('.'):
                continue
                
            for platform_dir in type_dir.iterdir():
                if not platform_dir.is_dir() or platform_dir.name.startswith('.'):
                    continue
                
                template_path = f"content/{type_dir.name}/{platform_dir.name}"
                templates.append(template_path)
        
        return templates
    
    def _scan_learning_templates(self, learning_dir: Path) -> List[str]:
        """학습 템플릿 스캔"""
        templates = []
        
        for type_dir in learning_dir.iterdir():
            if not type_dir.is_dir() or type_dir.name.startswith('.'):
                continue
                
            template_path = f"learning/{type_dir.name}"
            templates.append(template_path)
        
        return templates
    
    def get_template_path(self, template_name: str) -> Optional[Path]:
        """템플릿 경로 반환"""
        if not self.ensure_cache_updated():
            return None
        
        template_path = self.templates_dir / "templates" / template_name
        
        if template_path.exists() and template_path.is_dir():
            return template_path
        
        return None
    
    def get_template_versions(self, template_name: str) -> List[str]:
        """템플릿 버전 목록 반환 (Git 태그 기반)"""
        if not is_git_available():
            return ["latest"]
        
        tags = get_remote_tags(self.repo_url)
        return ["latest"] + tags
    
    def get_template_with_version(self, template_name: str, version: str) -> Optional[Path]:
        """특정 버전의 템플릿 반환"""
        if version == "latest":
            return self.get_template_path(template_name)
        
        # 버전별 캐시 디렉토리
        version_cache_dir = self.cache_dir / "versions" / version
        version_templates_dir = version_cache_dir / "templates"
        
        # 버전 캐시가 없으면 생성
        if not version_templates_dir.exists():
            if not clone_specific_tag(self.repo_url, version, version_cache_dir):
                return None
        
        template_path = version_templates_dir / "templates" / template_name
        
        if template_path.exists() and template_path.is_dir():
            return template_path
        
        return None
    
    def get_template_info(self, template_name: str) -> Optional[Dict[str, Any]]:
        """템플릿 정보 반환"""
        template_path = self.get_template_path(template_name)
        
        if not template_path:
            return None
        
        # 템플릿 정보 파일 확인
        info_file = template_path / "template.yaml"
        if not info_file.exists():
            info_file = template_path / "template.yml"
        
        if info_file.exists():
            from ..utils.file_utils import load_yaml_file
            return load_yaml_file(info_file)
        
        # 기본 정보 반환
        return {
            "name": template_name,
            "description": f"Template for {template_name}",
            "version": "latest",
            "path": str(template_path)
        }
    
    def validate_template(self, template_path: Path) -> bool:
        """템플릿 유효성 검사"""
        # 필수 파일 확인
        required_files = []
        
        # AGENT.md 또는 README.md 중 하나는 있어야 함
        if not (template_path / "AGENT.md").exists() and not (template_path / "README.md").exists():
            print_warning(f"템플릿 {template_path.name}에 AGENT.md 또는 README.md 파일이 없습니다.")
            return False
        
        return True
    
    def clear_cache(self) -> bool:
        """캐시 삭제"""
        try:
            if self.cache_dir.exists():
                safe_remove(self.cache_dir)
                print_info("템플릿 캐시가 삭제되었습니다.")
            return True
        except Exception as e:
            print_error(f"캐시 삭제 중 오류 발생: {e}")
            return False
    
    def get_cache_info(self) -> Dict[str, Any]:
        """캐시 정보 반환"""
        cache_info_file = self.cache_dir / "cache_info.json"
        
        if cache_info_file.exists():
            try:
                import json
                with open(cache_info_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        
        return {
            "last_update": "Never",
            "repo_url": self.repo_url,
            "branch": self.branch,
            "cache_size": self._get_cache_size()
        }
    
    def _get_cache_size(self) -> str:
        """캐시 크기 계산"""
        if not self.cache_dir.exists():
            return "0 MB"
        
        total_size = 0
        for path in self.cache_dir.rglob('*'):
            if path.is_file():
                total_size += path.stat().st_size
        
        # MB 단위로 변환
        size_mb = total_size / (1024 * 1024)
        return f"{size_mb:.1f} MB"


# 전역 템플릿 매니저 인스턴스
template_manager = TemplateManager()


# 레거시 함수들 (이전 버전 호환성)
def get_available_templates() -> List[str]:
    """사용 가능한 템플릿 목록 반환 (레거시)"""
    all_templates = template_manager.get_available_templates()
    result = []
    
    for category, templates in all_templates.items():
        result.extend(templates)
    
    return result


def get_template_versions(template_name: str) -> List[str]:
    """템플릿 버전 목록 반환 (레거시)"""
    return template_manager.get_template_versions(template_name)