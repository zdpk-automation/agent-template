"""
유틸리티 패키지 (Utilities Package)
"""
from .ui_utils import (
    print_success, print_error, print_info, print_warning,
    print_panel, show_progress, confirm, input_text, input_email,
    select_template_category, select_development_language, select_development_framework,
    select_content_type, select_content_platform, select_learning_type,
    display_project_info, display_next_steps, display_template_structure
)
from .file_utils import (
    create_directory, copy_file, copy_directory, create_symlink,
    set_read_only, is_read_only, substitute_placeholders, process_template_file,
    create_template_metadata, load_template_metadata, get_directory_structure,
    cleanup_empty_directories, safe_remove
)
from .git_utils import (
    is_git_available, clone_repository, get_remote_tags, get_remote_branches,
    clone_specific_tag, update_repository, get_repository_info
)

__all__ = [
    # UI utilities
    "print_success", "print_error", "print_info", "print_warning",
    "print_panel", "show_progress", "confirm", "input_text", "input_email",
    "select_template_category", "select_development_language", "select_development_framework",
    "select_content_type", "select_content_platform", "select_learning_type",
    "display_project_info", "display_next_steps", "display_template_structure",
    
    # File utilities
    "create_directory", "copy_file", "copy_directory", "create_symlink",
    "set_read_only", "is_read_only", "substitute_placeholders", "process_template_file",
    "create_template_metadata", "load_template_metadata", "get_directory_structure",
    "cleanup_empty_directories", "safe_remove",
    
    # Git utilities
    "is_git_available", "clone_repository", "get_remote_tags", "get_remote_branches",
    "clone_specific_tag", "update_repository", "get_repository_info",
]