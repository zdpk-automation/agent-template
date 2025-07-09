"""
초기화 명령어 (Initialization Command)
"""
import typer
from pathlib import Path
from typing import Optional
from typing_extensions import Annotated

from ..config import settings
from ..core.project_generator import project_generator
from ..core.template_manager import template_manager
from ..utils import (
    print_success, print_error, print_info, print_warning, confirm,
    input_text, input_email, select_template_category, select_development_language,
    select_development_framework, select_content_type, select_content_platform,
    select_learning_type, display_project_info, display_next_steps,
    display_template_structure
)

app = typer.Typer()


@app.command(name="interactive")
def interactive_init():
    """
    대화형 프로젝트 초기화
    Interactive project initialization
    """
    try:
        print_info("🚀 Agent Template CLI - 대화형 프로젝트 초기화")
        print_info("🚀 Agent Template CLI - Interactive Project Initialization")
        
        # 1. 템플릿 카테고리 선택
        category = select_template_category()
        if not category:
            print_error("템플릿 카테고리를 선택해주세요.")
            raise typer.Exit(code=1)
        
        # 2. 세부 템플릿 선택
        template_name = _select_specific_template(category)
        if not template_name:
            print_error("템플릿을 선택해주세요.")
            raise typer.Exit(code=1)
        
        # 3. 프로젝트 정보 입력
        project_info = _collect_project_info(template_name)
        
        # 4. 프로젝트 정보 확인
        display_project_info(project_info)
        
        if not confirm("이 정보로 프로젝트를 생성하시겠습니까?"):
            print_info("프로젝트 생성이 취소되었습니다.")
            raise typer.Exit(code=0)
        
        # 5. 프로젝트 생성
        success = project_generator.generate_project(
            template_name=template_name,
            project_name=project_info["name"],
            version=project_info.get("version", "latest"),
            context={
                "author_name": project_info["author"],
                "author_email": project_info["email"],
                "project_name": project_info["name"]
            }
        )
        
        if success:
            # 6. 다음 단계 안내
            project_dir = Path.cwd() / project_info["name"]
            next_steps = project_generator.get_next_steps(
                template_name, project_info["name"], project_dir
            )
            display_next_steps(next_steps)
            
            # 7. 프로젝트 구조 표시
            if confirm("생성된 프로젝트 구조를 확인하시겠습니까?"):
                structure = project_generator.get_project_structure(project_dir)
                display_template_structure(structure)
        else:
            print_error("프로젝트 생성에 실패했습니다.")
            raise typer.Exit(code=1)
            
    except KeyboardInterrupt:
        print_info("\n프로젝트 생성이 중단되었습니다.")
        raise typer.Exit(code=1)
    except Exception as e:
        print_error(f"예상치 못한 오류가 발생했습니다: {e}")
        raise typer.Exit(code=1)


@app.command(name="project")
def project_init(
    template_name: Annotated[str, typer.Argument(help="사용할 템플릿 이름 (예: development/python/fastapi)")],
    project_name: Annotated[str, typer.Argument(help="새 프로젝트 이름")],
    version: Annotated[str, typer.Option("--version", "-v", help="템플릿 버전 (Git 태그). 기본값: latest")] = "latest",
    author: Annotated[Optional[str], typer.Option("--author", "-a", help="작성자 이름")] = None,
    email: Annotated[Optional[str], typer.Option("--email", "-e", help="작성자 이메일")] = None,
    output_dir: Annotated[Optional[str], typer.Option("--output", "-o", help="출력 디렉토리")] = None,
    force: Annotated[bool, typer.Option("--force", "-f", help="기존 디렉토리가 있어도 덮어쓰기")] = False,
):
    """
    지정된 템플릿으로 새 프로젝트 초기화
    Initialize a new project from a specified template
    """
    try:
        # 템플릿 존재 확인
        available_templates = template_manager.get_available_templates()
        all_templates = []
        for category, templates in available_templates.items():
            all_templates.extend(templates)
        
        if template_name not in all_templates:
            print_error(f"템플릿 '{template_name}'을 찾을 수 없습니다.")
            print_info("사용 가능한 템플릿:")
            for category, templates in available_templates.items():
                print_info(f"  {category}:")
                for template in templates:
                    print_info(f"    - {template}")
            raise typer.Exit(code=1)
        
        # 버전 확인
        if version != "latest":
            available_versions = template_manager.get_template_versions(template_name)
            if version not in available_versions:
                print_error(f"버전 '{version}'을 찾을 수 없습니다.")
                print_info(f"사용 가능한 버전: {', '.join(available_versions)}")
                raise typer.Exit(code=1)
        
        # 출력 디렉토리 설정
        if output_dir:
            project_dir = Path(output_dir) / project_name
        else:
            project_dir = Path.cwd() / project_name
        
        # 기존 디렉토리 확인
        if project_dir.exists() and not force:
            print_error(f"프로젝트 디렉토리 '{project_dir}'가 이미 존재합니다.")
            print_info("--force 옵션을 사용하여 덮어쓸 수 있습니다.")
            raise typer.Exit(code=1)
        
        # 작성자 정보 수집
        if not author or not email:
            saved_author = settings.get_author_info()
            if not author:
                author = saved_author.get("name", "")
            if not email:
                email = saved_author.get("email", "")
        
        # 컨텍스트 준비
        context = {
            "author_name": author or "Unknown",
            "author_email": email or "unknown@example.com",
            "project_name": project_name
        }
        
        # 기존 디렉토리 삭제 (force 옵션)
        if project_dir.exists() and force:
            import shutil
            shutil.rmtree(project_dir)
            print_info(f"기존 디렉토리 '{project_dir}' 삭제됨")
        
        # 프로젝트 생성
        success = project_generator.generate_project(
            template_name=template_name,
            project_name=project_name,
            project_dir=project_dir,
            version=version,
            context=context
        )
        
        if success:
            print_success(f"프로젝트 '{project_name}'이 성공적으로 생성되었습니다!")
            print_info(f"템플릿: {template_name} (버전: {version})")
            print_info(f"위치: {project_dir}")
            
            # 다음 단계 안내
            next_steps = project_generator.get_next_steps(template_name, project_name, project_dir)
            display_next_steps(next_steps)
        else:
            print_error("프로젝트 생성에 실패했습니다.")
            raise typer.Exit(code=1)
            
    except Exception as e:
        print_error(f"프로젝트 초기화 중 오류 발생: {e}")
        raise typer.Exit(code=1)


@app.callback()
def init_callback():
    """
    프로젝트 초기화 명령어
    Project initialization commands
    """
    pass


def _select_specific_template(category: str) -> Optional[str]:
    """카테고리별 구체적인 템플릿 선택"""
    if category == "development":
        return _select_development_template()
    elif category == "content":
        return _select_content_template()
    elif category == "learning":
        return _select_learning_template()
    return None


def _select_development_template() -> Optional[str]:
    """개발 템플릿 선택"""
    # 언어 선택
    language = select_development_language()
    if not language:
        return None
    
    # 프레임워크 선택
    framework = select_development_framework(language)
    if not framework:
        return None
    
    return f"development/{language}/{framework}"


def _select_content_template() -> Optional[str]:
    """콘텐츠 템플릿 선택"""
    # 콘텐츠 타입 선택
    content_type = select_content_type()
    if not content_type:
        return None
    
    # 플랫폼 선택
    platform = select_content_platform(content_type)
    if not platform:
        return None
    
    return f"content/{content_type}/{platform}"


def _select_learning_template() -> Optional[str]:
    """학습 템플릿 선택"""
    # 학습 타입 선택
    learning_type = select_learning_type()
    if not learning_type:
        return None
    
    return f"learning/{learning_type}"


def _collect_project_info(template_name: str) -> dict:
    """프로젝트 정보 수집"""
    print_info("📝 프로젝트 정보를 입력해주세요.")
    
    # 프로젝트 이름
    project_name = input_text("프로젝트 이름을 입력하세요 (Enter project name):")
    if not project_name:
        print_error("프로젝트 이름을 입력해주세요.")
        raise typer.Exit(code=1)
    
    # 작성자 정보 (설정에서 기본값 가져오기)
    saved_author = settings.get_author_info()
    
    author_name = input_text(
        "작성자 이름을 입력하세요 (Enter author name):",
        default=saved_author.get("name", "")
    )
    
    author_email = input_email(
        "작성자 이메일을 입력하세요 (Enter author email):",
        default=saved_author.get("email", "")
    )
    
    # 작성자 정보 저장 여부 확인
    if author_name and author_email:
        if saved_author.get("name") != author_name or saved_author.get("email") != author_email:
            if confirm("이 작성자 정보를 기본값으로 저장하시겠습니까?"):
                settings.set_author_info(author_name, author_email)
                print_info("작성자 정보가 저장되었습니다.")
    
    # 버전 선택 (선택사항)
    versions = template_manager.get_template_versions(template_name)
    if len(versions) > 1:
        print_info(f"사용 가능한 버전: {', '.join(versions)}")
        version = input_text("버전을 입력하세요 (기본값: latest):", default="latest")
        if version not in versions:
            print_warning(f"버전 '{version}'이 존재하지 않습니다. 'latest'를 사용합니다.")
            version = "latest"
    else:
        version = "latest"
    
    return {
        "name": project_name,
        "author": author_name,
        "email": author_email,
        "template": template_name,
        "version": version,
        "path": f"./{project_name}/"
    }


# 기본 명령어를 interactive로 설정
@app.command(name="", hidden=True)
def default():
    """기본 init 명령어 (대화형)"""
    interactive_init()


if __name__ == "__main__":
    app()