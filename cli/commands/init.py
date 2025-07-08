import typer
from typing_extensions import Annotated

from cli.core.project_generator import generate_project
from cli.core.template_manager import get_available_templates, get_template_versions
from cli.utils import print_success, print_error

app = typer.Typer()

@app.command()
def project(
    template_name: Annotated[str, typer.Argument(help="Name of the template to use.")],
    project_name: Annotated[str, typer.Argument(help="Name of the new project.")],
    version: Annotated[str, typer.Option("--version", "-v", help="Template version (Git tag). Defaults to latest.")] = "latest",
):
    """
    Initialize a new project from a specified template.
    """
    available_templates = get_available_templates()
    if template_name not in available_templates:
        print_error(f"Template '{template_name}' not found. Available templates: {', '.join(available_templates)}")
        raise typer.Exit(code=1)

    if version != "latest":
        available_versions = get_template_versions(template_name)
        if version not in available_versions:
            print_error(f"Version '{version}' not found for template '{template_name}'. Available versions: {', '.join(available_versions)}")
            raise typer.Exit(code=1)

    try:
        generate_project(template_name, project_name, version)
        print_success(f"Project '{project_name}' initialized successfully from template '{template_name}' (version: {version}).")
    except Exception as e:
        print_error(f"Failed to initialize project: {e}")
        raise typer.Exit(code=1)