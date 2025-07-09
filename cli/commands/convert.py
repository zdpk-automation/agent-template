"""
변환 명령어 (Convert Command)
"""
import typer
from pathlib import Path
from typing import Optional
from typing_extensions import Annotated

from ..config import settings
from ..core.template_manager import template_manager
from ..utils import (
    print_success, print_error, print_info, print_warning, confirm,
    select_content_platform, display_project_info
)

app = typer.Typer()


@app.command()
def platform(
    source_platform: Annotated[str, typer.Argument(help="소스 플랫폼 (youtube, instagram, x, threads)")],
    target_platform: Annotated[str, typer.Argument(help="대상 플랫폼 (youtube, instagram, x, threads)")],
    content_path: Annotated[str, typer.Argument(help="변환할 콘텐츠 경로")],
    output_path: Annotated[Optional[str], typer.Option("--output", "-o", help="출력 경로")] = None,
    force: Annotated[bool, typer.Option("--force", "-f", help="기존 파일이 있어도 덮어쓰기")] = False,
):
    """
    플랫폼 간 콘텐츠 변환
    Convert content between platforms
    """
    try:
        # 플랫폼 유효성 검사
        supported_platforms = ["youtube", "instagram", "x", "threads"]
        
        if source_platform not in supported_platforms:
            print_error(f"지원되지 않는 소스 플랫폼: {source_platform}")
            print_info(f"지원되는 플랫폼: {', '.join(supported_platforms)}")
            raise typer.Exit(code=1)
        
        if target_platform not in supported_platforms:
            print_error(f"지원되지 않는 대상 플랫폼: {target_platform}")
            print_info(f"지원되는 플랫폼: {', '.join(supported_platforms)}")
            raise typer.Exit(code=1)
        
        if source_platform == target_platform:
            print_error("소스 플랫폼과 대상 플랫폼이 같습니다.")
            raise typer.Exit(code=1)
        
        # 콘텐츠 파일 확인
        content_file = Path(content_path)
        if not content_file.exists():
            print_error(f"콘텐츠 파일을 찾을 수 없습니다: {content_path}")
            raise typer.Exit(code=1)
        
        # 출력 경로 설정
        if output_path:
            output_file = Path(output_path)
        else:
            output_file = content_file.parent / f"{content_file.stem}_{target_platform}{content_file.suffix}"
        
        # 기존 파일 확인
        if output_file.exists() and not force:
            print_error(f"출력 파일이 이미 존재합니다: {output_file}")
            print_info("--force 옵션을 사용하여 덮어쓸 수 있습니다.")
            raise typer.Exit(code=1)
        
        print_info(f"플랫폼 변환 시작: {source_platform} → {target_platform}")
        print_info(f"입력 파일: {content_file}")
        print_info(f"출력 파일: {output_file}")
        
        # 변환 규칙 적용
        converted_content = _convert_content(
            content_file, source_platform, target_platform
        )
        
        # 출력 파일 저장
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(converted_content)
        
        print_success(f"콘텐츠 변환이 완료되었습니다!")
        print_info(f"변환된 파일: {output_file}")
        
    except Exception as e:
        print_error(f"콘텐츠 변환 중 오류 발생: {e}")
        raise typer.Exit(code=1)


@app.command()
def interactive():
    """
    대화형 플랫폼 변환
    Interactive platform conversion
    """
    try:
        print_info("🔄 Agent Template CLI - 대화형 플랫폼 변환")
        print_info("🔄 Agent Template CLI - Interactive Platform Conversion")
        
        # 소스 플랫폼 선택
        source_platform = select_content_platform("소스 플랫폼을 선택하세요:")
        if not source_platform:
            print_error("소스 플랫폼을 선택해주세요.")
            raise typer.Exit(code=1)
        
        # 대상 플랫폼 선택
        target_platform = select_content_platform("대상 플랫폼을 선택하세요:")
        if not target_platform:
            print_error("대상 플랫폼을 선택해주세요.")
            raise typer.Exit(code=1)
        
        if source_platform == target_platform:
            print_error("소스 플랫폼과 대상 플랫폼이 같습니다.")
            raise typer.Exit(code=1)
        
        # 콘텐츠 파일 입력
        content_path = typer.prompt("변환할 콘텐츠 파일 경로를 입력하세요")
        content_file = Path(content_path)
        
        if not content_file.exists():
            print_error(f"콘텐츠 파일을 찾을 수 없습니다: {content_path}")
            raise typer.Exit(code=1)
        
        # 출력 경로 선택
        default_output = content_file.parent / f"{content_file.stem}_{target_platform}{content_file.suffix}"
        output_path = typer.prompt(
            "출력 파일 경로를 입력하세요 (기본값: 현재 디렉토리)",
            default=str(default_output)
        )
        
        output_file = Path(output_path)
        
        # 변환 정보 확인
        conversion_info = {
            "소스 플랫폼": source_platform,
            "대상 플랫폼": target_platform,
            "입력 파일": str(content_file),
            "출력 파일": str(output_file)
        }
        
        print_info("🔄 변환 정보:")
        for key, value in conversion_info.items():
            print_info(f"  {key}: {value}")
        
        if not confirm("이 설정으로 변환을 진행하시겠습니까?"):
            print_info("변환이 취소되었습니다.")
            raise typer.Exit(code=0)
        
        # 변환 실행
        converted_content = _convert_content(
            content_file, source_platform, target_platform
        )
        
        # 출력 파일 저장
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(converted_content)
        
        print_success("콘텐츠 변환이 완료되었습니다!")
        print_info(f"변환된 파일: {output_file}")
        
    except KeyboardInterrupt:
        print_info("\n변환이 중단되었습니다.")
        raise typer.Exit(code=1)
    except Exception as e:
        print_error(f"예상치 못한 오류가 발생했습니다: {e}")
        raise typer.Exit(code=1)


def _convert_content(content_file: Path, source_platform: str, target_platform: str) -> str:
    """콘텐츠 변환 로직"""
    try:
        # 파일 읽기
        with open(content_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 플랫폼별 변환 규칙 적용
        converted_content = content
        
        # YouTube → Instagram 변환
        if source_platform == "youtube" and target_platform == "instagram":
            converted_content = _convert_youtube_to_instagram(content)
        
        # Instagram → YouTube 변환
        elif source_platform == "instagram" and target_platform == "youtube":
            converted_content = _convert_instagram_to_youtube(content)
        
        # X(Twitter) → Instagram 변환
        elif source_platform == "x" and target_platform == "instagram":
            converted_content = _convert_x_to_instagram(content)
        
        # Instagram → X(Twitter) 변환
        elif source_platform == "instagram" and target_platform == "x":
            converted_content = _convert_instagram_to_x(content)
        
        # Threads → Instagram 변환
        elif source_platform == "threads" and target_platform == "instagram":
            converted_content = _convert_threads_to_instagram(content)
        
        # Instagram → Threads 변환
        elif source_platform == "instagram" and target_platform == "threads":
            converted_content = _convert_instagram_to_threads(content)
        
        # 기타 변환 조합
        else:
            converted_content = _apply_generic_conversion(content, source_platform, target_platform)
        
        return converted_content
        
    except Exception as e:
        print_error(f"콘텐츠 변환 중 오류 발생: {e}")
        raise


def _convert_youtube_to_instagram(content: str) -> str:
    """YouTube 콘텐츠를 Instagram용으로 변환"""
    # 긴 형식을 짧은 형식으로 변환
    lines = content.split('\n')
    converted_lines = []
    
    for line in lines:
        # 제목 처리 (# → 간단한 텍스트)
        if line.startswith('#'):
            converted_lines.append(line.replace('#', '').strip())
        # 긴 문단을 짧은 문장으로 분할
        elif len(line) > 100:
            words = line.split()
            current_line = ""
            for word in words:
                if len(current_line + word) < 100:
                    current_line += word + " "
                else:
                    converted_lines.append(current_line.strip())
                    current_line = word + " "
            if current_line.strip():
                converted_lines.append(current_line.strip())
        else:
            converted_lines.append(line)
    
    return '\n'.join(converted_lines)


def _convert_instagram_to_youtube(content: str) -> str:
    """Instagram 콘텐츠를 YouTube용으로 변환"""
    # 짧은 형식을 긴 형식으로 확장
    lines = content.split('\n')
    converted_lines = []
    
    # 제목 추가
    converted_lines.append("# YouTube 콘텐츠")
    converted_lines.append("")
    
    for line in lines:
        if line.strip():
            # 각 라인을 더 자세히 설명
            converted_lines.append(f"## {line}")
            converted_lines.append("")
            converted_lines.append("이 부분에 대한 자세한 설명을 추가하세요.")
            converted_lines.append("")
    
    return '\n'.join(converted_lines)


def _convert_x_to_instagram(content: str) -> str:
    """X(Twitter) 콘텐츠를 Instagram용으로 변환"""
    # 해시태그 처리 및 이미지 친화적으로 변환
    content = content.replace('#', '\n#')
    return content


def _convert_instagram_to_x(content: str) -> str:
    """Instagram 콘텐츠를 X(Twitter)용으로 변환"""
    # 280자 제한에 맞춰 축약
    if len(content) > 280:
        content = content[:277] + "..."
    return content


def _convert_threads_to_instagram(content: str) -> str:
    """Threads 콘텐츠를 Instagram용으로 변환"""
    # 유사한 플랫폼이므로 최소한의 변환
    return content


def _convert_instagram_to_threads(content: str) -> str:
    """Instagram 콘텐츠를 Threads용으로 변환"""
    # 유사한 플랫폼이므로 최소한의 변환
    return content


def _apply_generic_conversion(content: str, source_platform: str, target_platform: str) -> str:
    """범용 변환 규칙 적용"""
    # 기본적인 변환 규칙
    converted_content = content
    
    # 플랫폼별 특수 문자 처리
    if target_platform == "x":
        # X(Twitter)는 짧은 형식 선호
        if len(converted_content) > 280:
            converted_content = converted_content[:277] + "..."
    
    elif target_platform == "instagram":
        # Instagram은 해시태그 친화적
        converted_content = converted_content.replace("\n\n", "\n")
    
    elif target_platform == "youtube":
        # YouTube는 긴 형식 선호
        if len(converted_content) < 500:
            converted_content += "\n\n더 자세한 내용을 추가하세요."
    
    return converted_content


@app.callback()
def convert_callback():
    """
    콘텐츠 변환 명령어
    Content conversion commands
    """
    pass


# 기본 명령어를 interactive로 설정
@app.command(name="", hidden=True)
def default():
    """기본 convert 명령어 (대화형)"""
    interactive()


if __name__ == "__main__":
    app()