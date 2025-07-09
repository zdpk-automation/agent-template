"""
Agent Template CLI - Main Entry Point / 메인 엔트리포인트
"""
import typer
from rich.console import Console

console = Console()

app = typer.Typer(
    name="agent-template",
    help="AI 에이전트 템플릿 관리 및 프로젝트 생성 도구 / AI agent template management and project generation tool",
    add_completion=False
)

@app.command()
def version():
    """
    Show CLI version / CLI 버전 정보 표시
    """
    console.print("Agent Template CLI v0.1.0", style="green")
    console.print("AI 에이전트 템플릿 관리 도구 / AI Agent Template Management Tool")

@app.callback()
def main():
    """
    🚀 Agent Template CLI
    
    AI 에이전트 템플릿을 활용한 프로젝트 생성 및 관리 도구
    Project generation and management tool using AI agent templates
    
    Usage Examples / 사용 예시:
      agent-template version    # Show version / 버전 확인
    """
    pass

if __name__ == "__main__":
    app()