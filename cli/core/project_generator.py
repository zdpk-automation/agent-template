# cli/core/project_generator.py

def generate_project(template_name: str, project_name: str, version: str = "latest"):
    """
    Generates a new project from the specified template.
    """
    print(f"Generating project '{project_name}' from template '{template_name}' (version: {version})")
