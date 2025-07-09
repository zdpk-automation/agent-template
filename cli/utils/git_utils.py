"""
Git 관련 유틸리티 (Git-related Utilities)
"""
import shutil
from pathlib import Path
from typing import List, Optional
import subprocess
import tempfile

from .ui_utils import print_error, print_info, show_progress


def is_git_available() -> bool:
    """Git이 설치되어 있는지 확인"""
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def clone_repository(repo_url: str, target_dir: Path, branch: str = "main") -> bool:
    """Git 저장소 클론"""
    try:
        print_info(f"저장소 클론 중: {repo_url}")
        show_progress("템플릿 다운로드 중...", 3.0)
        
        # 임시 디렉토리에 클론
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir) / "repo"
            
            # 얕은 클론으로 최신 커밋만 가져오기
            cmd = [
                'git', 'clone', 
                '--depth', '1',
                '--branch', branch,
                repo_url, 
                str(tmp_path)
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print_error(f"저장소 클론 실패: {result.stderr}")
                return False
            
            # .git 디렉토리 제거
            git_dir = tmp_path / ".git"
            if git_dir.exists():
                shutil.rmtree(git_dir)
            
            # 대상 디렉토리로 복사
            if target_dir.exists():
                shutil.rmtree(target_dir)
            
            shutil.copytree(tmp_path, target_dir)
            
        print_info(f"저장소 클론 완료: {target_dir}")
        return True
        
    except Exception as e:
        print_error(f"저장소 클론 중 오류 발생: {e}")
        return False


def get_remote_tags(repo_url: str) -> List[str]:
    """원격 저장소의 태그 목록 가져오기"""
    try:
        cmd = ['git', 'ls-remote', '--tags', repo_url]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        tags = []
        for line in result.stdout.strip().split('\n'):
            if line and 'refs/tags/' in line:
                # refs/tags/v1.0.0 형태에서 태그 이름만 추출
                tag = line.split('refs/tags/')[-1]
                # ^{} 형태 제거 (annotated tag)
                if not tag.endswith('^{}'):
                    tags.append(tag)
        
        return sorted(tags, reverse=True)  # 최신 태그부터
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []


def get_remote_branches(repo_url: str) -> List[str]:
    """원격 저장소의 브랜치 목록 가져오기"""
    try:
        cmd = ['git', 'ls-remote', '--heads', repo_url]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        branches = []
        for line in result.stdout.strip().split('\n'):
            if line and 'refs/heads/' in line:
                # refs/heads/main 형태에서 브랜치 이름만 추출
                branch = line.split('refs/heads/')[-1]
                branches.append(branch)
        
        return sorted(branches)
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []


def clone_specific_tag(repo_url: str, tag: str, target_dir: Path) -> bool:
    """특정 태그로 저장소 클론"""
    try:
        print_info(f"태그 {tag}로 저장소 클론 중: {repo_url}")
        show_progress(f"태그 {tag} 다운로드 중...", 3.0)
        
        # 임시 디렉토리에 클론
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir) / "repo"
            
            # 특정 태그로 얕은 클론
            cmd = [
                'git', 'clone',
                '--depth', '1',
                '--branch', tag,
                repo_url,
                str(tmp_path)
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print_error(f"태그 {tag} 클론 실패: {result.stderr}")
                return False
            
            # .git 디렉토리 제거
            git_dir = tmp_path / ".git"
            if git_dir.exists():
                shutil.rmtree(git_dir)
            
            # 대상 디렉토리로 복사
            if target_dir.exists():
                shutil.rmtree(target_dir)
            
            shutil.copytree(tmp_path, target_dir)
            
        print_info(f"태그 {tag} 클론 완료: {target_dir}")
        return True
        
    except Exception as e:
        print_error(f"태그 {tag} 클론 중 오류 발생: {e}")
        return False


def update_repository(repo_dir: Path, repo_url: str, branch: str = "main") -> bool:
    """저장소 업데이트"""
    try:
        print_info(f"저장소 업데이트 중: {repo_dir}")
        
        # 기존 디렉토리 제거 후 재클론
        if repo_dir.exists():
            shutil.rmtree(repo_dir)
        
        return clone_repository(repo_url, repo_dir, branch)
        
    except Exception as e:
        print_error(f"저장소 업데이트 중 오류 발생: {e}")
        return False


def get_current_commit_hash(repo_dir: Path) -> Optional[str]:
    """현재 커밋 해시 가져오기"""
    try:
        cmd = ['git', 'rev-parse', 'HEAD']
        result = subprocess.run(
            cmd, 
            cwd=repo_dir, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def get_repository_info(repo_dir: Path) -> Optional[dict]:
    """저장소 정보 가져오기"""
    try:
        if not (repo_dir / ".git").exists():
            return None
        
        # 원격 URL 가져오기
        cmd = ['git', 'config', '--get', 'remote.origin.url']
        result = subprocess.run(
            cmd, 
            cwd=repo_dir, 
            capture_output=True, 
            text=True, 
            check=True
        )
        remote_url = result.stdout.strip()
        
        # 현재 브랜치 가져오기
        cmd = ['git', 'branch', '--show-current']
        result = subprocess.run(
            cmd, 
            cwd=repo_dir, 
            capture_output=True, 
            text=True, 
            check=True
        )
        current_branch = result.stdout.strip()
        
        # 커밋 해시 가져오기
        commit_hash = get_current_commit_hash(repo_dir)
        
        return {
            "remote_url": remote_url,
            "current_branch": current_branch,
            "commit_hash": commit_hash
        }
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None