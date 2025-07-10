"""
Git operations / Git 작업
"""
import subprocess
import shutil
from pathlib import Path
from typing import List, Optional

from git import Repo, GitCommandError


def is_git_available() -> bool:
    """Check if git is available / Git 사용 가능 여부 확인"""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def clone_repository(repo_url: str, target_dir: Path, branch: str = "main") -> bool:
    """Clone repository / 저장소 클론"""
    try:
        if target_dir.exists():
            shutil.rmtree(target_dir)
        
        target_dir.parent.mkdir(parents=True, exist_ok=True)
        Repo.clone_from(repo_url, target_dir, branch=branch, depth=1)
        return True
    except GitCommandError as e:
        print(f"Failed to clone repository: {e}")
        return False


def update_repository(repo_dir: Path, repo_url: str, branch: str = "main") -> bool:
    """Update existing repository / 기존 저장소 업데이트"""
    try:
        if not repo_dir.exists():
            return clone_repository(repo_url, repo_dir, branch)
        
        repo = Repo(repo_dir)
        origin = repo.remotes.origin
        origin.fetch()
        
        # Reset to remote branch / 원격 브랜치로 리셋
        repo.git.reset('--hard', f'origin/{branch}')
        return True
    except GitCommandError as e:
        print(f"Failed to update repository: {e}")
        # If update fails, try to re-clone / 업데이트 실패 시 재클론 시도
        return clone_repository(repo_url, repo_dir, branch)


def get_remote_tags(repo_url: str) -> List[str]:
    """Get remote repository tags / 원격 저장소 태그 목록 반환"""
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--tags", repo_url],
            capture_output=True,
            text=True,
            check=True
        )
        
        tags = []
        for line in result.stdout.strip().split('\n'):
            if line and 'refs/tags/' in line:
                tag = line.split('refs/tags/')[-1]
                if not tag.endswith('^{}'):  # Skip annotated tag refs
                    tags.append(tag)
        
        return sorted(tags, reverse=True)
    except subprocess.CalledProcessError:
        return []


def clone_specific_tag(repo_url: str, tag: str, target_dir: Path) -> bool:
    """Clone repository at specific tag / 특정 태그로 저장소 클론"""
    try:
        if target_dir.exists():
            shutil.rmtree(target_dir)
        
        target_dir.parent.mkdir(parents=True, exist_ok=True)
        
        # Clone with specific tag / 특정 태그로 클론
        repo = Repo.clone_from(repo_url, target_dir, branch=tag, depth=1)
        return True
    except GitCommandError as e:
        print(f"Failed to clone tag {tag}: {e}")
        return False


def get_repository_info(repo_dir: Path) -> Optional[dict]:
    """Get repository information / 저장소 정보 반환"""
    try:
        if not repo_dir.exists():
            return None
        
        repo = Repo(repo_dir)
        return {
            "url": repo.remotes.origin.url,
            "branch": repo.active_branch.name,
            "commit": repo.head.commit.hexsha[:8],
            "last_commit_date": repo.head.commit.committed_datetime.isoformat()
        }
    except Exception:
        return None


def safe_remove(path: Path) -> bool:
    """Safely remove directory or file / 디렉토리나 파일 안전 삭제"""
    try:
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)
        return True
    except Exception as e:
        print(f"Failed to remove {path}: {e}")
        return False