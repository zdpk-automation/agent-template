"""
업데이트 명령어 (Update Command)
"""
import typer
from pathlib import Path
from typing import Optional
from typing_extensions import Annotated

from ..config import settings
from ..core.template_manager import template_manager
from ..utils import (
    print_success, print_error, print_info, print_warning, confirm,
    show_progress, display_project_info
)

app = typer.Typer()


@app.command()
def template(
    project_path: Annotated[str, typer.Argument(help="업데이트할 프로젝트 경로")],
    version: Annotated[str, typer.Option("--version", "-v", help="업데이트할 버전 (Git 태그). 기본값: latest")] = "latest",
    force: Annotated[bool, typer.Option("--force", "-f", help="강제 업데이트 (보호된 파일도 덮어쓰기)")] = False,
    dry_run: Annotated[bool, typer.Option("--dry-run", "-d", help="실제 업데이트 없이 변경 사항만 미리보기")] = False,
):
    """
    프로젝트 템플릿 업데이트
    Update project template
    """
    try:
        project_dir = Path(project_path)
        
        # 프로젝트 디렉토리 확인
        if not project_dir.exists():
            print_error(f"프로젝트 디렉토리를 찾을 수 없습니다: {project_path}")
            raise typer.Exit(code=1)
        
        # 템플릿 메타데이터 확인
        metadata_file = project_dir / ".agent" / "template" / "metadata.json"
        if not metadata_file.exists():
            print_error("이 프로젝트는 Agent Template로 생성된 프로젝트가 아닙니다.")
            print_info("템플릿 메타데이터 파일을 찾을 수 없습니다.")
            raise typer.Exit(code=1)
        
        # 메타데이터 읽기
        import json
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        template_name = metadata.get('template_type')
        current_version = metadata.get('version', 'unknown')
        
        print_info(f"📦 프로젝트 템플릿 업데이트")
        print_info(f"  프로젝트: {project_dir.name}")
        print_info(f"  현재 템플릿: {template_name}")
        print_info(f"  현재 버전: {current_version}")
        print_info(f"  대상 버전: {version}")
        
        # 버전 확인
        if version == current_version:
            print_warning("현재 버전과 동일한 버전으로 업데이트하려고 합니다.")
            if not confirm("계속 진행하시겠습니까?"):
                print_info("업데이트가 취소되었습니다.")
                raise typer.Exit(code=0)
        
        # 템플릿 존재 확인
        template_path = template_manager.get_template_with_version(template_name, version)
        if not template_path:
            print_error(f"템플릿 '{template_name}' (버전: {version})을 찾을 수 없습니다.")
            raise typer.Exit(code=1)
        
        # 변경 사항 분석
        changes = _analyze_changes(project_dir, template_path, metadata)
        
        if not changes:
            print_success("업데이트할 내용이 없습니다.")
            raise typer.Exit(code=0)
        
        # 변경 사항 표시
        print_info("\n📋 변경 사항:")
        for change in changes:
            status_icon = {
                'added': '✅',
                'modified': '🔄',
                'removed': '❌'
            }.get(change['type'], '❓')
            print_info(f"  {status_icon} {change['type'].upper()}: {change['file']}")
        
        # Dry run 모드
        if dry_run:
            print_info("\n🔍 Dry run 모드: 실제 변경 사항 없이 미리보기만 표시됩니다.")
            raise typer.Exit(code=0)
        
        # 업데이트 확인
        if not confirm("\n이 변경 사항을 적용하시겠습니까?"):
            print_info("업데이트가 취소되었습니다.")
            raise typer.Exit(code=0)
        
        # 백업 생성
        backup_dir = project_dir / ".agent" / "backups" / f"backup_{metadata.get('version', 'unknown')}"
        _create_backup(project_dir, backup_dir)
        print_info(f"백업 생성: {backup_dir}")
        
        # 업데이트 실행
        success = _apply_update(project_dir, template_path, metadata, force)
        
        if success:
            # 메타데이터 업데이트
            metadata['version'] = version
            metadata['last_updated'] = _get_current_timestamp()
            
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            print_success(f"템플릿 업데이트가 완료되었습니다!")
            print_info(f"업데이트 버전: {version}")
            print_info(f"백업 위치: {backup_dir}")
        else:
            print_error("템플릿 업데이트에 실패했습니다.")
            raise typer.Exit(code=1)
        
    except Exception as e:
        print_error(f"템플릿 업데이트 중 오류 발생: {e}")
        raise typer.Exit(code=1)


@app.command()
def cache():
    """
    템플릿 캐시 업데이트
    Update template cache
    """
    try:
        print_info("🔄 템플릿 캐시 업데이트 중...")
        
        # 강제 캐시 업데이트
        success = template_manager.ensure_cache_updated(force=True)
        
        if success:
            print_success("템플릿 캐시가 성공적으로 업데이트되었습니다!")
            
            # 캐시 정보 표시
            cache_info = template_manager.get_cache_info()
            print_info("\n📦 업데이트된 캐시 정보:")
            print_info(f"  마지막 업데이트: {cache_info.get('last_update', 'Never')}")
            print_info(f"  저장소 URL: {cache_info.get('repo_url', 'N/A')}")
            print_info(f"  브랜치: {cache_info.get('branch', 'N/A')}")
            print_info(f"  캐시 크기: {cache_info.get('cache_size', 'N/A')}")
        else:
            print_error("템플릿 캐시 업데이트에 실패했습니다.")
            raise typer.Exit(code=1)
        
    except Exception as e:
        print_error(f"캐시 업데이트 중 오류 발생: {e}")
        raise typer.Exit(code=1)


@app.command()
def check(
    project_path: Annotated[str, typer.Argument(help="확인할 프로젝트 경로")],
):
    """
    프로젝트 업데이트 가능 여부 확인
    Check if project can be updated
    """
    try:
        project_dir = Path(project_path)
        
        # 프로젝트 디렉토리 확인
        if not project_dir.exists():
            print_error(f"프로젝트 디렉토리를 찾을 수 없습니다: {project_path}")
            raise typer.Exit(code=1)
        
        # 템플릿 메타데이터 확인
        metadata_file = project_dir / ".agent" / "template" / "metadata.json"
        if not metadata_file.exists():
            print_error("이 프로젝트는 Agent Template로 생성된 프로젝트가 아닙니다.")
            raise typer.Exit(code=1)
        
        # 메타데이터 읽기
        import json
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        template_name = metadata.get('template_type')
        current_version = metadata.get('version', 'unknown')
        
        print_info(f"🔍 프로젝트 업데이트 확인")
        print_info(f"  프로젝트: {project_dir.name}")
        print_info(f"  템플릿: {template_name}")
        print_info(f"  현재 버전: {current_version}")
        
        # 사용 가능한 버전 확인
        available_versions = template_manager.get_template_versions(template_name)
        print_info(f"  사용 가능한 버전: {', '.join(available_versions)}")
        
        # 최신 버전 확인
        latest_version = "latest"
        if current_version != latest_version:
            print_warning(f"새 버전을 사용할 수 있습니다: {latest_version}")
            print_info("다음 명령어로 업데이트할 수 있습니다:")
            print_info(f"  agent-template update template {project_path} --version {latest_version}")
        else:
            print_success("현재 최신 버전을 사용하고 있습니다.")
        
    except Exception as e:
        print_error(f"업데이트 확인 중 오류 발생: {e}")
        raise typer.Exit(code=1)


def _analyze_changes(project_dir: Path, template_path: Path, metadata: dict) -> list:
    """업데이트 변경 사항 분석"""
    changes = []
    
    try:
        # 제외할 파일/디렉토리 패턴
        exclude_patterns = [
            ".git",
            "__pycache__",
            "*.pyc",
            ".DS_Store",
            "Thumbs.db",
            ".agent",
            "venv",
            "node_modules"
        ]
        
        # 보호된 파일 목록
        protected_files = metadata.get('protected_files', [])
        
        # 템플릿 파일 순회
        for template_file in template_path.rglob("*"):
            if template_file.is_file():
                rel_path = template_file.relative_to(template_path)
                
                # 제외 패턴 확인
                if any(template_file.match(pattern) for pattern in exclude_patterns):
                    continue
                
                project_file = project_dir / rel_path
                
                if not project_file.exists():
                    changes.append({
                        'type': 'added',
                        'file': str(rel_path),
                        'protected': str(rel_path) in protected_files
                    })
                elif _files_differ(template_file, project_file):
                    changes.append({
                        'type': 'modified',
                        'file': str(rel_path),
                        'protected': str(rel_path) in protected_files
                    })
        
        return changes
        
    except Exception as e:
        print_error(f"변경 사항 분석 중 오류 발생: {e}")
        return []


def _files_differ(file1: Path, file2: Path) -> bool:
    """두 파일이 다른지 확인"""
    try:
        # 파일 크기 비교
        if file1.stat().st_size != file2.stat().st_size:
            return True
        
        # 텍스트 파일인 경우 내용 비교
        if file1.suffix in ['.md', '.txt', '.py', '.js', '.ts', '.html', '.css', '.json', '.yaml', '.yml']:
            with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
                return f1.read() != f2.read()
        
        # 바이너리 파일인 경우 해시 비교
        import hashlib
        
        def get_file_hash(filepath):
            hasher = hashlib.md5()
            with open(filepath, 'rb') as f:
                hasher.update(f.read())
            return hasher.hexdigest()
        
        return get_file_hash(file1) != get_file_hash(file2)
        
    except Exception:
        return True  # 오류 시 다른 것으로 간주


def _create_backup(project_dir: Path, backup_dir: Path):
    """프로젝트 백업 생성"""
    try:
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        # 백업할 파일 복사
        import shutil
        
        exclude_dirs = ['.git', '__pycache__', 'venv', 'node_modules', '.agent/backups']
        
        for item in project_dir.rglob("*"):
            if item.is_file():
                rel_path = item.relative_to(project_dir)
                
                # 제외 디렉토리 확인
                if any(part in exclude_dirs for part in rel_path.parts):
                    continue
                
                backup_file = backup_dir / rel_path
                backup_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, backup_file)
        
    except Exception as e:
        print_warning(f"백업 생성 중 오류 발생: {e}")


def _apply_update(project_dir: Path, template_path: Path, metadata: dict, force: bool) -> bool:
    """업데이트 적용"""
    try:
        from ..utils.file_utils import process_template_file, copy_file
        
        # 보호된 파일 목록
        protected_files = metadata.get('protected_files', [])
        
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
        
        # 컨텍스트 준비
        context = {
            "project_name": project_dir.name,
            "author_name": metadata.get('author', ''),
            "author_email": metadata.get('author_email', ''),
            "template_name": metadata.get('template_type', ''),
            "template_version": metadata.get('version', '')
        }
        
        # 템플릿 파일 업데이트
        for template_file in template_path.rglob("*"):
            if template_file.is_file():
                rel_path = template_file.relative_to(template_path)
                
                # 제외 패턴 확인
                if any(template_file.match(pattern) for pattern in exclude_patterns):
                    continue
                
                project_file = project_dir / rel_path
                
                # 보호된 파일 확인
                if str(rel_path) in protected_files and not force:
                    print_info(f"보호된 파일 스킵: {rel_path}")
                    continue
                
                # 파일 처리
                if template_file.suffix in ['.md', '.txt', '.py', '.js', '.ts', '.html', '.css', '.json', '.yaml', '.yml']:
                    # 텍스트 파일은 플레이스홀더 치환
                    process_template_file(template_file, project_file, context)
                else:
                    # 바이너리 파일은 그대로 복사
                    copy_file(template_file, project_file)
        
        return True
        
    except Exception as e:
        print_error(f"업데이트 적용 중 오류 발생: {e}")
        return False


def _get_current_timestamp() -> str:
    """현재 시간 스탬프 반환"""
    from datetime import datetime
    return datetime.now().isoformat()


@app.callback()
def update_callback():
    """
    업데이트 명령어
    Update commands
    """
    pass


if __name__ == "__main__":
    app()