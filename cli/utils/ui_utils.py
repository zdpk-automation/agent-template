"""
UI/UX utilities / UI/UX 유틸리티
"""
from rich.console import Console

console = Console()


def print_success(message: str) -> None:
    """Print success message / 성공 메시지 출력"""
    console.print(f"✅ {message}", style="green")


def print_error(message: str) -> None:
    """Print error message / 오류 메시지 출력"""
    console.print(f"❌ {message}", style="red")


def print_info(message: str) -> None:
    """Print info message / 정보 메시지 출력"""
    console.print(f"ℹ️  {message}", style="blue")


def print_warning(message: str) -> None:
    """Print warning message / 경고 메시지 출력"""
    console.print(f"⚠️  {message}", style="yellow")