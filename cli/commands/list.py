import typer

from cli.core.template_manager import get_available_templates, get_template_versions
from cli.utils import print_success

app = typer.Typer()

@app.command()
def templates():
    """
    List available templates and their versions.
    """
    print_success("Available Templates:")
    templates = get_available_templates()
    for template in templates:
        print(f"- {template}")
        versions = get_template_versions(template)
        if versions:
            print(f"  Versions: {', '.join(versions)}")
        else:
            print("  No specific versions found.")