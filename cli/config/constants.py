"""
Constants and default values / 상수 및 기본값
"""
from pathlib import Path

# Template categories / 템플릿 카테고리
TEMPLATE_CATEGORIES = {
    "development": "개발 프로젝트 / Development Projects",
    "content": "콘텐츠 생성 / Content Creation", 
    "learning": "학습 자료 / Learning Materials"
}

# Development languages / 개발 언어
DEVELOPMENT_LANGUAGES = {
    "python": "Python",
    "typescript": "TypeScript/JavaScript",
    "rust": "Rust"
}

# Development frameworks / 개발 프레임워크
DEVELOPMENT_FRAMEWORKS = {
    "python": {
        "fastapi": "FastAPI - Modern web API framework",
        "django": "Django - Full-featured web framework", 
        "typer": "Typer - CLI application framework"
    },
    "typescript": {
        "nextjs": "Next.js - React-based web framework",
        "nestjs": "NestJS - Node.js backend framework"
    },
    "rust": {
        "clap": "Clap - Command line argument parser",
        "axum": "Axum - Web application framework"
    }
}

# Content types / 콘텐츠 타입
CONTENT_TYPES = {
    "blog": "블로그 포스트 / Blog Posts",
    "documentation": "문서화 / Documentation",
    "tutorial": "튜토리얼 / Tutorials"
}

# Content platforms / 콘텐츠 플랫폼
CONTENT_PLATFORMS = {
    "blog": {
        "markdown": "Markdown files",
        "notion": "Notion pages",
        "obsidian": "Obsidian vault"
    },
    "documentation": {
        "mkdocs": "MkDocs",
        "gitbook": "GitBook",
        "sphinx": "Sphinx"
    }
}

# Learning types / 학습 타입
LEARNING_TYPES = {
    "course": "온라인 코스 / Online Course",
    "workshop": "워크샵 / Workshop",
    "study": "스터디 자료 / Study Materials"
}

# Default settings / 기본 설정
DEFAULT_REPO_URL = "https://github.com/zdpk-automation/agent-template.git"
DEFAULT_BRANCH = "main"
DEFAULT_CACHE_DIR = Path.home() / ".agent-template" / "cache"
CACHE_UPDATE_INTERVAL = 24 * 60 * 60  # 24 hours in seconds / 24시간(초)

# File protection / 파일 보호
PROTECTED_FILES = ["AGENT.md", "README.md", "CLAUDE.md", "GEMINI.md"]
AGENT_DIR = ".agent"
TEMPLATE_DIR = "template"
TEMPLATE_METADATA_FILE = "metadata.json"