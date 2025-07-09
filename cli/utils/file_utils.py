"""
파일 관련 유틸리티 (File-related Utilities)
"""
import os
import shutil
import stat
from pathlib import Path
from typing import Dict, Any, List, Optional
import json
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

from ..config.constants import PLACEHOLDERS, PROTECTED_FILE_PERMISSIONS, TEMPLATE_METADATA_FILE, AGENT_DIR, TEMPLATE_DIR


def create_directory(path: Path, parents: bool = True) -> None:
    """디렉토리 생성"""
    path.mkdir(parents=parents, exist_ok=True)


def copy_file(src: Path, dst: Path, create_dirs: bool = True) -> None:
    """파일 복사"""
    if create_dirs:
        dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def copy_directory(src: Path, dst: Path, ignore_patterns: Optional[List[str]] = None) -> None:
    """디렉토리 복사 (패턴 제외 가능)"""
    if ignore_patterns:
        ignore_func = shutil.ignore_patterns(*ignore_patterns)
    else:
        ignore_func = None
    
    shutil.copytree(src, dst, ignore=ignore_func, dirs_exist_ok=True)


def create_symlink(src: Path, dst: Path, create_dirs: bool = True) -> None:
    """심볼릭 링크 생성"""
    if create_dirs:
        dst.parent.mkdir(parents=True, exist_ok=True)
    
    # 기존 파일/링크가 있으면 제거
    if dst.exists() or dst.is_symlink():
        dst.unlink()
    
    os.symlink(src, dst)


def set_read_only(path: Path) -> None:
    """파일을 읽기 전용으로 설정"""
    os.chmod(path, PROTECTED_FILE_PERMISSIONS)


def is_read_only(path: Path) -> bool:
    """파일이 읽기 전용인지 확인"""
    return not os.access(path, os.W_OK)


def substitute_placeholders(content: str, context: Dict[str, Any]) -> str:
    """플레이스홀더 치환"""
    # 현재 날짜 정보 추가
    current_date = datetime.now()
    default_context = {
        "current_date": current_date.strftime("%Y-%m-%d"),
        "current_year": current_date.year,
    }
    
    # 컨텍스트 병합
    full_context = {**default_context, **context}
    
    # Jinja2 환경 설정
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    # 템플릿 렌더링
    template = env.from_string(content)
    return template.render(**full_context)


def process_template_file(src_path: Path, dst_path: Path, context: Dict[str, Any]) -> None:
    """템플릿 파일 처리 (플레이스홀더 치환 후 저장)"""
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 플레이스홀더 치환
    processed_content = substitute_placeholders(content, context)
    
    # 대상 디렉토리 생성
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 파일 저장
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(processed_content)


def create_template_metadata(project_dir: Path, template_info: Dict[str, Any]) -> None:
    """템플릿 메타데이터 파일 생성"""
    agent_dir = project_dir / AGENT_DIR
    agent_dir.mkdir(parents=True, exist_ok=True)
    
    metadata_file = agent_dir / TEMPLATE_METADATA_FILE
    
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(template_info, f, indent=2, ensure_ascii=False)


def load_template_metadata(project_dir: Path) -> Optional[Dict[str, Any]]:
    """템플릿 메타데이터 로드"""
    metadata_file = project_dir / AGENT_DIR / TEMPLATE_METADATA_FILE
    
    if not metadata_file.exists():
        return None
    
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def load_yaml_file(path: Path) -> Optional[Dict[str, Any]]:
    """YAML 파일 로드"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except (yaml.YAMLError, IOError):
        return None


def save_yaml_file(path: Path, data: Dict[str, Any]) -> None:
    """YAML 파일 저장"""
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def get_directory_structure(path: Path, max_depth: int = 3) -> Dict[str, Any]:
    """디렉토리 구조 분석"""
    def _scan_directory(dir_path: Path, current_depth: int = 0) -> Dict[str, Any]:
        if current_depth >= max_depth:
            return {}
        
        structure = {}
        
        try:
            for item in sorted(dir_path.iterdir()):
                if item.is_dir():
                    structure[item.name] = _scan_directory(item, current_depth + 1)
                else:
                    structure[item.name] = "file"
        except PermissionError:
            pass
        
        return structure
    
    return _scan_directory(path)


def cleanup_empty_directories(path: Path) -> None:
    """빈 디렉토리 정리"""
    for item in path.rglob('*'):
        if item.is_dir() and not any(item.iterdir()):
            try:
                item.rmdir()
            except OSError:
                pass


def ensure_executable(path: Path) -> None:
    """파일을 실행 가능하게 설정"""
    current_mode = path.stat().st_mode
    path.chmod(current_mode | stat.S_IEXEC)


def get_file_size(path: Path) -> int:
    """파일 크기 반환 (바이트)"""
    return path.stat().st_size


def get_file_modified_time(path: Path) -> datetime:
    """파일 수정 시간 반환"""
    return datetime.fromtimestamp(path.stat().st_mtime)


def is_binary_file(path: Path) -> bool:
    """바이너리 파일인지 확인"""
    try:
        with open(path, 'rb') as f:
            chunk = f.read(1024)
            return b'\0' in chunk
    except IOError:
        return False


def find_files_by_pattern(directory: Path, pattern: str) -> List[Path]:
    """패턴으로 파일 찾기"""
    return list(directory.rglob(pattern))


def safe_remove(path: Path) -> None:
    """안전하게 파일/디렉토리 제거"""
    try:
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    except (OSError, IOError):
        pass