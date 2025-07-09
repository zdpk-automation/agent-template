"""
UI/UX 유틸리티 (UI/UX Utilities)
"""
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing import List, Dict, Any, Optional
import time

from ..config.constants import TEMPLATE_CATEGORIES, DEVELOPMENT_LANGUAGES, DEVELOPMENT_FRAMEWORKS, CONTENT_TYPES, CONTENT_PLATFORMS, LEARNING_TYPES

console = Console()


def print_success(message: str) -> None:
    """성공 메시지 출력"""
    console.print(f"✅ {message}", style="green")


def print_error(message: str) -> None:
    """오류 메시지 출력"""
    console.print(f"❌ {message}", style="red")


def print_info(message: str) -> None:
    """정보 메시지 출력"""
    console.print(f"ℹ️  {message}", style="blue")


def print_warning(message: str) -> None:
    """경고 메시지 출력"""
    console.print(f"⚠️  {message}", style="yellow")


def print_panel(title: str, content: str, style: str = "blue") -> None:
    """패널 형태로 메시지 출력"""
    panel = Panel(content, title=title, style=style)
    console.print(panel)


def select_template_category() -> str:
    """템플릿 카테고리 선택"""
    choices = [
        questionary.Choice(title=f"{value}", value=key)
        for key, value in TEMPLATE_CATEGORIES.items()
    ]
    
    return questionary.select(
        "어떤 유형의 프로젝트를 시작하시겠습니까? (What type of project would you like to start?)",
        choices=choices,
        style=questionary.Style([
            ('question', 'bold'),
            ('pointer', 'fg:#ff0066 bold'),
            ('highlighted', 'fg:#ff0066 bold'),
            ('answer', 'fg:#44ff00 bold'),
        ])
    ).ask()


def select_development_language() -> str:
    """개발 언어 선택"""
    choices = [
        questionary.Choice(title=f"{value}", value=key)
        for key, value in DEVELOPMENT_LANGUAGES.items()
    ]
    
    return questionary.select(
        "개발 언어를 선택하세요 (Select programming language):",
        choices=choices
    ).ask()


def select_development_framework(language: str) -> str:
    """개발 프레임워크 선택"""
    frameworks = DEVELOPMENT_FRAMEWORKS.get(language, {})
    
    choices = [
        questionary.Choice(title=f"{value}", value=key)
        for key, value in frameworks.items()
    ]
    
    return questionary.select(
        "프레임워크를 선택하세요 (Select framework):",
        choices=choices
    ).ask()


def select_content_type() -> str:
    """콘텐츠 유형 선택"""
    choices = [
        questionary.Choice(title=f"{value}", value=key)
        for key, value in CONTENT_TYPES.items()
    ]
    
    return questionary.select(
        "콘텐츠 유형을 선택하세요 (Select content type):",
        choices=choices
    ).ask()


def select_content_platform(content_type: str = None, message: str = None) -> str:
    """콘텐츠 플랫폼 선택"""
    if content_type:
        platforms = CONTENT_PLATFORMS.get(content_type, {})
        choices = [
            questionary.Choice(title=f"{value}", value=key)
            for key, value in platforms.items()
        ]
        prompt = message or "플랫폼을 선택하세요 (Select platform):"
    else:
        # 모든 플랫폼 표시
        all_platforms = ["youtube", "instagram", "x", "threads"]
        choices = [
            questionary.Choice(title=platform.capitalize(), value=platform)
            for platform in all_platforms
        ]
        prompt = message or "플랫폼을 선택하세요 (Select platform):"
    
    return questionary.select(prompt, choices=choices).ask()


def select_learning_type() -> str:
    """학습 유형 선택"""
    choices = [
        questionary.Choice(title=f"{value}", value=key)
        for key, value in LEARNING_TYPES.items()
    ]
    
    return questionary.select(
        "학습 유형을 선택하세요 (Select learning type):",
        choices=choices
    ).ask()


def input_text(message: str, default: str = "") -> str:
    """텍스트 입력"""
    return questionary.text(message, default=default).ask()


def input_email(message: str, default: str = "") -> str:
    """이메일 입력 (간단한 검증 포함)"""
    def validate_email(text: str) -> bool:
        return "@" in text and "." in text.split("@")[-1]
    
    return questionary.text(
        message,
        default=default,
        validate=lambda text: validate_email(text) or "유효한 이메일 주소를 입력해주세요."
    ).ask()


def confirm(message: str, default: bool = True) -> bool:
    """확인 메시지"""
    return questionary.confirm(message, default=default).ask()


def show_progress(description: str, duration: float = 2.0) -> None:
    """진행률 표시"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task(description, total=None)
        time.sleep(duration)
        progress.update(task, completed=True)


def display_project_info(project_info: Dict[str, Any]) -> None:
    """프로젝트 정보 표시"""
    info_text = Text()
    info_text.append(f"프로젝트 이름: {project_info['name']}\n", style="bold")
    info_text.append(f"작성자: {project_info['author']}\n")
    info_text.append(f"이메일: {project_info['email']}\n")
    info_text.append(f"템플릿: {project_info['template']}\n")
    info_text.append(f"생성 위치: {project_info['path']}\n")
    
    panel = Panel(info_text, title="프로젝트 정보 (Project Information)", style="green")
    console.print(panel)


def display_next_steps(steps: List[str]) -> None:
    """다음 단계 표시"""
    steps_text = Text()
    for i, step in enumerate(steps, 1):
        steps_text.append(f"{i}. {step}\n")
    
    panel = Panel(steps_text, title="다음 단계 (Next Steps)", style="blue")
    console.print(panel)


def display_template_structure(structure: Dict[str, Any]) -> None:
    """템플릿 구조 표시"""
    def format_structure(data: Dict[str, Any], indent: int = 0) -> str:
        result = ""
        for key, value in data.items():
            prefix = "  " * indent + "├── " if indent > 0 else ""
            if isinstance(value, dict):
                result += f"{prefix}{key}/\n"
                result += format_structure(value, indent + 1)
            else:
                result += f"{prefix}{key}\n"
        return result
    
    structure_text = format_structure(structure)
    panel = Panel(structure_text, title="생성된 파일 구조 (Generated File Structure)", style="cyan")
    console.print(panel)