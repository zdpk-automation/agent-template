"""
프로젝트 생성 (Project Generation)
"""
import os
import shutil
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime

from ..config import settings
from ..config.constants import AGENT_DIR, TEMPLATE_DIR, TEMPLATE_METADATA_FILE
from ..utils import (
    print_info, print_error, print_success, print_warning, show_progress,
    create_directory, copy_file, copy_directory, create_symlink, set_read_only,
    substitute_placeholders, process_template_file, create_template_metadata,
    get_directory_structure, cleanup_empty_directories
)
from .template_manager import template_manager


class ProjectGenerator:
    """프로젝트 생성기 클래스"""
    
    def __init__(self):
        self.template_manager = template_manager
    
    def generate_project(
        self, 
        template_name: str, 
        project_name: str, 
        project_dir: Optional[Path] = None,
        version: str = "latest",
        context: Optional[Dict[str, Any]] = None
    ) -> bool:
        """프로젝트 생성"""
        try:
            # 기본 프로젝트 디렉토리 설정
            if project_dir is None:
                project_dir = Path.cwd() / project_name
            
            # 프로젝트 디렉토리가 이미 존재하는지 확인
            if project_dir.exists():
                print_error(f"프로젝트 디렉토리 '{project_dir}'가 이미 존재합니다.")
                return False
            
            # 템플릿 경로 가져오기
            template_path = self.template_manager.get_template_with_version(template_name, version)
            if not template_path:
                print_error(f"템플릿 '{template_name}' (버전: {version})을 찾을 수 없습니다.")
                return False
            
            # 템플릿 유효성 검사
            if not self.template_manager.validate_template(template_path):
                print_error(f"템플릿 '{template_name}'이 유효하지 않습니다.")
                return False
            
            print_info(f"프로젝트 '{project_name}' 생성 중...")
            show_progress("템플릿 복사 중...", 2.0)
            
            # 프로젝트 디렉토리 생성
            create_directory(project_dir)
            
            # 컨텍스트 준비
            if context is None:
                context = {}
            
            context.update({
                "project_name": project_name,
                "template_version": version,
                "template_name": template_name
            })
            
            # 템플릿 파일 복사 및 처리
            success = self._copy_template_files(template_path, project_dir, context)
            if not success:
                # 실패 시 생성된 디렉토리 정리
                if project_dir.exists():
                    shutil.rmtree(project_dir)
                return False
            
            # 보호된 파일 심볼릭 링크 생성
            protected_files = self._create_protected_files(template_path, project_dir)
            
            # 템플릿 메타데이터 생성
            metadata = {
                "version": version,
                "template_type": template_name,
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "author": context.get("author_name", ""),
                "author_email": context.get("author_email", ""),
                "project_name": project_name,
                "protected_files": protected_files
            }
            
            create_template_metadata(project_dir, metadata)
            
            # 빈 디렉토리 정리
            cleanup_empty_directories(project_dir)
            
            print_success(f"프로젝트 '{project_name}'가 성공적으로 생성되었습니다!")
            print_info(f"위치: {project_dir}")
            
            return True
            
        except Exception as e:
            print_error(f"프로젝트 생성 중 오류 발생: {e}")
            # 실패 시 생성된 디렉토리 정리
            if project_dir and project_dir.exists():
                shutil.rmtree(project_dir)
            return False
    
    def _copy_template_files(self, template_path: Path, project_dir: Path, context: Dict[str, Any]) -> bool:
        """템플릿 파일 복사 및 처리"""
        try:
            # 제외할 파일/디렉토리 패턴
            exclude_patterns = [
                ".git",
                "__pycache__",
                "*.pyc",
                ".DS_Store",
                "Thumbs.db",
                "template.yaml",
                "template.yml",
                ".template"
            ]
            
            # 보호된 파일 목록 (나중에 심볼릭 링크로 처리)
            protected_files = ["AGENT.md", "README.md", "CLAUDE.md", "GEMINI.md"]
            
            for item in template_path.rglob("*"):
                if item.is_file():
                    # 상대 경로 계산
                    rel_path = item.relative_to(template_path)
                    
                    # 제외 패턴 확인
                    if any(item.match(pattern) for pattern in exclude_patterns):
                        continue
                    
                    # 대상 경로
                    target_path = project_dir / rel_path
                    
                    # 보호된 파일은 스킵 (나중에 심볼릭 링크로 처리)
                    if item.name in protected_files:
                        continue
                    
                    # 파일 처리
                    if item.suffix in ['.md', '.txt', '.py', '.js', '.ts', '.html', '.css', '.json', '.yaml', '.yml', '.toml']:
                        # 텍스트 파일은 플레이스홀더 치환
                        process_template_file(item, target_path, context)
                    else:
                        # 바이너리 파일은 그대로 복사
                        copy_file(item, target_path)
            
            return True
            
        except Exception as e:
            print_error(f"템플릿 파일 복사 중 오류 발생: {e}")
            return False
    
    def _create_protected_files(self, template_path: Path, project_dir: Path) -> List[str]:
        """보호된 파일 심볼릭 링크 생성"""
        protected_files = []
        
        # .agent/template 디렉토리 생성
        agent_template_dir = project_dir / AGENT_DIR / TEMPLATE_DIR
        create_directory(agent_template_dir)
        
        # 보호할 파일 목록
        files_to_protect = [
            "AGENT.md",
            "README.md", 
            "CLAUDE.md",
            "GEMINI.md"
        ]
        
        for filename in files_to_protect:
            template_file = template_path / filename
            if template_file.exists():
                # 캐시에서 보호된 파일 복사
                cache_file = agent_template_dir / filename
                copy_file(template_file, cache_file)
                
                # 읽기 전용 권한 설정
                set_read_only(cache_file)
                
                # 프로젝트 루트에 심볼릭 링크 생성
                link_path = project_dir / filename
                try:
                    create_symlink(cache_file, link_path)
                    protected_files.append(str(link_path.relative_to(project_dir)))
                    print_info(f"보호된 파일 생성: {filename}")
                except Exception as e:
                    print_warning(f"심볼릭 링크 생성 실패 ({filename}): {e}")
                    # 심볼릭 링크 실패 시 일반 복사
                    copy_file(cache_file, link_path)
                    protected_files.append(str(link_path.relative_to(project_dir)))
        
        return protected_files
    
    def get_next_steps(self, template_name: str, project_name: str, project_dir: Path) -> List[str]:
        """다음 단계 안내"""
        steps = [f"cd {project_name}"]
        
        # 템플릿 타입에 따른 다음 단계
        if "python" in template_name:
            steps.extend([
                "python -m venv venv",
                "source venv/bin/activate  # Linux/Mac",
                "# 또는 venv\\Scripts\\activate  # Windows",
                "pip install -r requirements.txt"
            ])
            
            if "fastapi" in template_name:
                steps.append("uvicorn main:app --reload")
            elif "django" in template_name:
                steps.extend([
                    "python manage.py migrate",
                    "python manage.py runserver"
                ])
            elif "flask" in template_name:
                steps.append("flask run")
            elif "typer" in template_name:
                steps.extend([
                    "pip install -e .",
                    f"{project_name} --help"
                ])
        
        elif "typescript" in template_name:
            steps.extend([
                "npm install",
                "npm run dev"
            ])
        
        elif "rust" in template_name:
            steps.extend([
                "cargo build",
                "cargo run"
            ])
        
        elif "content" in template_name:
            if "obsidian" in template_name:
                steps.extend([
                    "Obsidian에서 폴더 열기",
                    "index.md 파일 편집 시작"
                ])
            else:
                steps.append("README.md 파일을 확인하고 편집을 시작하세요")
        
        else:
            steps.append("README.md 파일을 확인하고 프로젝트를 시작하세요")
        
        return steps
    
    def get_project_structure(self, project_dir: Path) -> Dict[str, Any]:
        """프로젝트 구조 반환"""
        return get_directory_structure(project_dir, max_depth=3)


# 전역 프로젝트 생성기 인스턴스
project_generator = ProjectGenerator()


# 레거시 함수 (이전 버전 호환성)
def generate_project(template_name: str, project_name: str, version: str = "latest"):
    """프로젝트 생성 (레거시)"""
    return project_generator.generate_project(template_name, project_name, version=version)