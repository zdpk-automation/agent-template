"""
설정 관리 (Settings Management)
"""
import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

from .constants import DEFAULT_CONFIG_DIR, DEFAULT_CACHE_DIR, DEFAULT_REPO_URL, DEFAULT_BRANCH


class Settings:
    """CLI 설정 관리 클래스"""
    
    def __init__(self, config_dir: Optional[Path] = None):
        self.config_dir = config_dir or DEFAULT_CONFIG_DIR
        self.config_file = self.config_dir / "config.json"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # 기본 설정
        self.defaults = {
            "cache_dir": str(DEFAULT_CACHE_DIR),
            "repo_url": DEFAULT_REPO_URL,
            "branch": DEFAULT_BRANCH,
            "author": {
                "name": "",
                "email": ""
            },
            "templates": {
                "auto_update": True,
                "update_interval": 3600
            },
            "ui": {
                "theme": "default",
                "show_progress": True
            }
        }
        
        self._config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """설정 파일 로드"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                # 기본 설정과 병합
                return {**self.defaults, **config}
            except (json.JSONDecodeError, IOError):
                return self.defaults.copy()
        return self.defaults.copy()
    
    def save_config(self) -> None:
        """설정 파일 저장"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self._config, f, indent=2, ensure_ascii=False)
    
    def get(self, key: str, default: Any = None) -> Any:
        """설정 값 가져오기 (점 표기법 지원)"""
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """설정 값 설정 (점 표기법 지원)"""
        keys = key.split('.')
        config = self._config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        self.save_config()
    
    def get_cache_dir(self) -> Path:
        """캐시 디렉토리 경로 반환"""
        return Path(self.get("cache_dir", str(DEFAULT_CACHE_DIR)))
    
    def get_repo_url(self) -> str:
        """저장소 URL 반환"""
        return self.get("repo_url", DEFAULT_REPO_URL)
    
    def get_branch(self) -> str:
        """브랜치 반환"""
        return self.get("branch", DEFAULT_BRANCH)
    
    def get_author_info(self) -> Dict[str, str]:
        """작성자 정보 반환"""
        return {
            "name": self.get("author.name", ""),
            "email": self.get("author.email", "")
        }
    
    def set_author_info(self, name: str, email: str) -> None:
        """작성자 정보 설정"""
        self.set("author.name", name)
        self.set("author.email", email)


# 전역 설정 인스턴스
settings = Settings()