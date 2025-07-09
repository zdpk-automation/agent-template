"""
상수 정의 (Constants Definition)
"""
import os
from pathlib import Path

# 기본 디렉토리 (Default Directories)
DEFAULT_CACHE_DIR = Path.home() / ".agent-template-cache"
DEFAULT_CONFIG_DIR = Path.home() / ".config" / "agent-template"

# 템플릿 카테고리 (Template Categories)
TEMPLATE_CATEGORIES = {
    "development": "개발 프로젝트 (Development)",
    "content": "콘텐츠 제작 (Content Creation)",
    "learning": "학습 프로젝트 (Learning)"
}

# 개발 템플릿 하위 카테고리 (Development Template Subcategories)
DEVELOPMENT_LANGUAGES = {
    "python": "Python",
    "typescript": "TypeScript",
    "rust": "Rust",
    "dart": "Dart"
}

DEVELOPMENT_FRAMEWORKS = {
    "python": {
        "fastapi": "FastAPI",
        "django": "Django",
        "flask": "Flask",
        "typer": "CLI (Typer)"
    },
    "typescript": {
        "nextjs": "Next.js",
        "express": "Express.js",
        "nestjs": "NestJS"
    },
    "rust": {
        "axum": "Axum",
        "clap": "CLI (Clap)"
    },
    "dart": {
        "flutter": "Flutter"
    }
}

# 콘텐츠 템플릿 하위 카테고리 (Content Template Subcategories)
CONTENT_TYPES = {
    "blog": "블로그 포스트",
    "social": "소셜 미디어",
    "video": "비디오 콘텐츠"
}

CONTENT_PLATFORMS = {
    "blog": {
        "obsidian": "Obsidian",
        "notion": "Notion",
        "markdown": "Markdown"
    },
    "social": {
        "youtube": "YouTube",
        "instagram": "Instagram",
        "x": "X/Twitter",
        "threads": "Threads"
    }
}

# 학습 템플릿 하위 카테고리 (Learning Template Subcategories)
LEARNING_TYPES = {
    "course": "강좌 (Course)",
    "research": "연구 (Research)",
    "project": "프로젝트 (Project)"
}

# 플레이스홀더 (Placeholders)
PLACEHOLDERS = {
    "project_name": "{{project_name}}",
    "author_name": "{{author_name}}",
    "author_email": "{{author_email}}",
    "current_date": "{{current_date}}",
    "current_year": "{{current_year}}",
    "template_version": "{{template_version}}"
}

# 파일 보호 설정 (File Protection Settings)
PROTECTED_FILE_PERMISSIONS = 0o444  # 읽기 전용
CACHE_UPDATE_INTERVAL = 3600  # 1시간 (초)

# Git 저장소 설정 (Git Repository Settings)
DEFAULT_REPO_URL = "https://github.com/zdpk-automation/agent-template.git"
DEFAULT_BRANCH = "main"

# 메타데이터 파일 (Metadata Files)
TEMPLATE_METADATA_FILE = "template.json"
AGENT_DIR = ".agent"
TEMPLATE_DIR = "template"