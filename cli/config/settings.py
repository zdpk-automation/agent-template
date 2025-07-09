"""
Settings management / 설정 관리
"""
import json
from pathlib import Path
from typing import Any, Dict, Optional

from .constants import DEFAULT_REPO_URL, DEFAULT_BRANCH, DEFAULT_CACHE_DIR


class Settings:
    """Settings manager / 설정 관리자"""
    
    def __init__(self):
        self.config_dir = Path.home() / ".agent-template"
        self.config_file = self.config_dir / "config.json"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self._config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file / 파일에서 설정 로드"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        
        return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration / 기본 설정 반환"""
        return {
            "repo_url": DEFAULT_REPO_URL,
            "branch": DEFAULT_BRANCH,
            "cache_dir": str(DEFAULT_CACHE_DIR),
            "author": {
                "name": "",
                "email": ""
            }
        }
    
    def save_config(self) -> None:
        """Save configuration to file / 설정을 파일에 저장"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Failed to save config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value / 설정값 가져오기"""
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value / 설정값 설정"""
        self._config[key] = value
        self.save_config()
    
    def get_repo_url(self) -> str:
        """Get repository URL / 저장소 URL 반환"""
        return self.get("repo_url", DEFAULT_REPO_URL)
    
    def get_branch(self) -> str:
        """Get repository branch / 저장소 브랜치 반환"""
        return self.get("branch", DEFAULT_BRANCH)
    
    def get_cache_dir(self) -> Path:
        """Get cache directory / 캐시 디렉토리 반환"""
        cache_dir = Path(self.get("cache_dir", str(DEFAULT_CACHE_DIR)))
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir
    
    def get_author_info(self) -> Dict[str, str]:
        """Get author information / 작성자 정보 반환"""
        return self.get("author", {"name": "", "email": ""})
    
    def set_author_info(self, name: str, email: str) -> None:
        """Set author information / 작성자 정보 설정"""
        self.set("author", {"name": name, "email": email})


# Global settings instance / 전역 설정 인스턴스
settings = Settings()