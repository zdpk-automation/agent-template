"""
Template management / 템플릿 관리
"""
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

from ..config import settings
from ..config.constants import CACHE_UPDATE_INTERVAL
from ..utils import (
    print_info, print_error, is_git_available, 
    clone_repository, update_repository, get_remote_tags
)


class TemplateManager:
    """Template manager / 템플릿 관리자"""
    
    def __init__(self):
        self.cache_dir = settings.get_cache_dir()
        self.templates_dir = self.cache_dir / "templates"
        self.repo_url = settings.get_repo_url()
        self.branch = settings.get_branch()
        
        # Create cache directory / 캐시 디렉토리 생성
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def ensure_cache_updated(self, force: bool = False) -> bool:
        """Ensure cache is up to date / 캐시가 최신 상태인지 확인"""
        if not is_git_available():
            print_error("Git is not installed. Please install Git.")
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
        """Update template cache / 템플릿 캐시 업데이트"""
        print_info("Updating template cache... / 템플릿 캐시 업데이트 중...")
        
        # Clone or update repository / 저장소 클론 또는 업데이트
        if self.templates_dir.exists():
            success = update_repository(self.templates_dir, self.repo_url, self.branch)
        else:
            success = clone_repository(self.repo_url, self.templates_dir, self.branch)
        
        if success:
            # Update cache info / 캐시 정보 업데이트
            cache_info = {
                "last_update": datetime.now().isoformat(),
                "repo_url": self.repo_url,
                "branch": self.branch
            }
            
            import json
            cache_info_file = self.cache_dir / "cache_info.json"
            with open(cache_info_file, 'w') as f:
                json.dump(cache_info, f, indent=2)
            
            print_info("Template cache updated successfully / 템플릿 캐시 업데이트 완료")
            return True
        
        return False
    
    def get_available_templates(self) -> Dict[str, List[str]]:
        """Get available templates / 사용 가능한 템플릿 목록 반환"""
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
        
        # Scan for templates / 템플릿 스캔
        for category_dir in templates_root.iterdir():
            if not category_dir.is_dir() or category_dir.name.startswith('.'):
                continue
            
            category = category_dir.name
            if category in templates:
                templates[category] = self._scan_category_templates(category_dir, category)
        
        return templates
    
    def _scan_category_templates(self, category_dir: Path, category: str) -> List[str]:
        """Scan templates in category / 카테고리별 템플릿 스캔"""
        templates = []
        
        if category == "development":
            # development/language/framework structure
            for lang_dir in category_dir.iterdir():
                if not lang_dir.is_dir() or lang_dir.name.startswith('.'):
                    continue
                
                for framework_dir in lang_dir.iterdir():
                    if not framework_dir.is_dir() or framework_dir.name.startswith('.'):
                        continue
                    
                    template_path = f"{category}/{lang_dir.name}/{framework_dir.name}"
                    templates.append(template_path)
        
        else:
            # Simple category/type structure for content and learning
            for type_dir in category_dir.iterdir():
                if not type_dir.is_dir() or type_dir.name.startswith('.'):
                    continue
                
                template_path = f"{category}/{type_dir.name}"
                templates.append(template_path)
        
        return templates
    
    def get_template_path(self, template_name: str) -> Optional[Path]:
        """Get template path / 템플릿 경로 반환"""
        if not self.ensure_cache_updated():
            return None
        
        template_path = self.templates_dir / "templates" / template_name
        
        if template_path.exists() and template_path.is_dir():
            return template_path
        
        return None
    
    def get_template_versions(self, template_name: str) -> List[str]:
        """Get template versions / 템플릿 버전 목록 반환"""
        if not is_git_available():
            return ["latest"]
        
        tags = get_remote_tags(self.repo_url)
        return ["latest"] + tags
    
    def validate_template(self, template_path: Path) -> bool:
        """Validate template / 템플릿 유효성 검사"""
        # Check for required files / 필수 파일 확인
        if not (template_path / "AGENT.md").exists() and not (template_path / "README.md").exists():
            return False
        
        return True
    
    def get_cache_info(self) -> Dict[str, Any]:
        """Get cache information / 캐시 정보 반환"""
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
        """Get cache size / 캐시 크기 계산"""
        if not self.cache_dir.exists():
            return "0 MB"
        
        total_size = 0
        for path in self.cache_dir.rglob('*'):
            if path.is_file():
                total_size += path.stat().st_size
        
        # Convert to MB / MB 단위로 변환
        size_mb = total_size / (1024 * 1024)
        return f"{size_mb:.1f} MB"


# Global template manager instance / 전역 템플릿 관리자 인스턴스
template_manager = TemplateManager()


# Legacy functions for compatibility / 호환성을 위한 레거시 함수
def get_available_templates() -> List[str]:
    """Get available templates (legacy) / 사용 가능한 템플릿 목록 반환 (레거시)"""
    all_templates = template_manager.get_available_templates()
    result = []
    
    for category, templates in all_templates.items():
        result.extend(templates)
    
    return result


def get_template_versions(template_name: str) -> List[str]:
    """Get template versions (legacy) / 템플릿 버전 목록 반환 (레거시)"""
    return template_manager.get_template_versions(template_name)