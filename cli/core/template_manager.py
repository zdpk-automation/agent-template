# cli/core/template_manager.py

def get_available_templates():
    """
    Fetches and returns a list of available templates.
    """
    return ["backend", "frontend", "fullstack"]

def get_template_versions(template_name: str):
    """
    Fetches and returns available versions for a given template.
    """
    return ["v1.0.0", "v1.1.0"]
