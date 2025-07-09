"""
레거시 유틸리티 (Legacy Utilities)
새로운 utils 패키지로 이동되었습니다.
"""
# 이전 버전과의 호환성을 위한 import
from .utils import print_success, print_error, print_info, print_warning

# 사용 중지 경고
import warnings
warnings.warn(
    "cli.utils is deprecated. Use cli.utils.ui_utils instead.",
    DeprecationWarning,
    stacklevel=2
)

__all__ = ["print_success", "print_error", "print_info", "print_warning"]