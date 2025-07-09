"""
Agent Template CLI - 메인 엔트리포인트
"""
import typer
from pathlib import Path
import sys

# 현재 디렉토리를 Python 경로에 추가
sys.path.insert(0, str(Path(__file__).parent))

from cli.commands import init, list as list_cmd, convert, update
from cli.config import settings
from cli.utils import print_info, print_error

app = typer.Typer(
    name="agent-template",
    help="AI 에이전트 템플릿 관리 및 프로젝트 생성 도구",
    add_completion=False
)

# 하위 명령어 등록
app.add_typer(init.app, name="init", help="프로젝트 초기화 (Initialize a new project)")
app.add_typer(list_cmd.app, name="list", help="템플릿 목록 조회 (List available templates)")
app.add_typer(convert.app, name="convert", help="콘텐츠 변환 (Convert content between platforms)")
app.add_typer(update.app, name="update", help="프로젝트 업데이트 (Update projects and cache)")

@app.command()
def version():
    """
    CLI 버전 정보 표시
    Show CLI version information
    """
    print_info("Agent Template CLI v1.0.0")
    print_info("AI 에이전트 템플릿 관리 도구")
    print_info("Repository: https://github.com/zdpk-automation/agent-template")


@app.command()
def cache():
    """
    캐시 관리
    Cache management
    """
    from cli.core.template_manager import template_manager
    
    cache_info = template_manager.get_cache_info()
    print_info("📦 템플릿 캐시 정보:")
    print_info(f"  마지막 업데이트: {cache_info.get('last_update', 'Never')}")
    print_info(f"  저장소 URL: {cache_info.get('repo_url', 'N/A')}")
    print_info(f"  브랜치: {cache_info.get('branch', 'N/A')}")
    print_info(f"  캐시 크기: {cache_info.get('cache_size', 'N/A')}")


@app.command()
def clear_cache():
    """
    캐시 삭제
    Clear cache
    """
    from cli.core.template_manager import template_manager
    from cli.utils import confirm
    
    if confirm("템플릿 캐시를 삭제하시겠습니까?"):
        if template_manager.clear_cache():
            print_info("캐시가 성공적으로 삭제되었습니다.")
        else:
            print_error("캐시 삭제에 실패했습니다.")
    else:
        print_info("캐시 삭제가 취소되었습니다.")


@app.command()
def config(
    key: str = typer.Argument(None, help="설정 키"),
    value: str = typer.Argument(None, help="설정 값")
):
    """
    설정 관리
    Configuration management
    """
    if key is None:
        # 전체 설정 표시
        print_info("⚙️ 현재 설정:")
        
        author_info = settings.get_author_info()
        print_info(f"  작성자 이름: {author_info.get('name', '설정되지 않음')}")
        print_info(f"  작성자 이메일: {author_info.get('email', '설정되지 않음')}")
        print_info(f"  캐시 디렉토리: {settings.get_cache_dir()}")
        print_info(f"  저장소 URL: {settings.get_repo_url()}")
        print_info(f"  브랜치: {settings.get_branch()}")
        
    elif value is None:
        # 특정 설정 값 표시
        config_value = settings.get(key)
        if config_value is not None:
            print_info(f"{key}: {config_value}")
        else:
            print_error(f"설정 '{key}'를 찾을 수 없습니다.")
    else:
        # 설정 값 변경
        settings.set(key, value)
        print_info(f"설정 '{key}'가 '{value}'로 변경되었습니다.")


@app.callback()
def main():
    """
    🚀 Agent Template CLI
    
    AI 에이전트 템플릿을 활용한 프로젝트 생성 및 관리 도구
    
    사용 예시:
      agent-template init                           # 대화형 프로젝트 초기화
      agent-template init project fastapi my-api   # 직접 프로젝트 생성
      agent-template list templates                # 템플릿 목록 조회
      agent-template convert                        # 대화형 콘텐츠 변환
      agent-template convert platform youtube instagram content.md  # 플랫폼 간 변환
      agent-template update cache                   # 템플릿 캐시 업데이트
      agent-template update template ./my-project   # 프로젝트 업데이트
      agent-template cache                          # 캐시 정보 확인
      agent-template config                         # 설정 확인
    """
    pass


if __name__ == "__main__":
    app()