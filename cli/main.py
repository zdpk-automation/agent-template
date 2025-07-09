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


@app.command()
def cache():
    """
    Show cache information / 캐시 정보 표시
    """
    from .core.template_manager import template_manager
    
    cache_info = template_manager.get_cache_info()
    console.print("📦 Template Cache Information / 템플릿 캐시 정보:", style="blue")
    console.print(f"  Last Update / 마지막 업데이트: {cache_info.get('last_update', 'Never')}")
    console.print(f"  Repository URL / 저장소 URL: {cache_info.get('repo_url', 'N/A')}")
    console.print(f"  Branch / 브랜치: {cache_info.get('branch', 'N/A')}")
    console.print(f"  Cache Size / 캐시 크기: {cache_info.get('cache_size', 'N/A')}")


@app.command()
def update_cache():
    """
    Update template cache / 템플릿 캐시 업데이트
    """
    from .core.template_manager import template_manager
    
    if template_manager.ensure_cache_updated(force=True):
        console.print("✅ Template cache updated successfully / 템플릿 캐시 업데이트 완료", style="green")
    else:
        console.print("❌ Failed to update template cache / 템플릿 캐시 업데이트 실패", style="red")

@app.callback()
def main():
    """
    🚀 Agent Template CLI
    
    AI 에이전트 템플릿을 활용한 프로젝트 생성 및 관리 도구
    Project generation and management tool using AI agent templates
    
    Usage Examples / 사용 예시:
      agent-template version        # Show version / 버전 확인
      agent-template cache          # Show cache info / 캐시 정보 확인
      agent-template update-cache   # Update cache / 캐시 업데이트
    """
    pass

if __name__ == "__main__":
    app()