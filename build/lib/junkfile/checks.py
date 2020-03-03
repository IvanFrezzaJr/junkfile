import os
import shutil


def check_exists(path: str):
    """Check exists
    
    Check if file or path exists.
    - os.F_OK: Tests existence of the path.

    Arguments:
        path {str} -- file or folder path
    
    Returns:
        bool --  returns True if exists
    """

    return os.access(path, os.F_OK) if path else False


def check_is_readable(path: str):
    """Check is readable
    
    Check if path or folder is readable.
    - os.R_OK: Tests readability of the path.

    Arguments:
        path {str} -- file or folder path
    
    Returns:
        bool --  returns True if is readable
    """

    return os.access(path, os.R_OK) if path else False


def check_is_writable(path: str):
    """Check is writable
    
    Check if path or folder is writable.
    - os.W_OK: Tests writability of the path.

    Arguments:
        path {str} -- file or folder path
    
    Returns:
        bool --  returns True if is writable
    """

    return os.access(path, os.W_OK) if path else False


def check_is_executable(path: str):
    """Check is executable
    
    Check if path or folder is executable.
    - os.X_OK: Checks if path can be executed.

    Arguments:
        path {str} -- file or folder path
    
    Returns:
        bool --  returns True if is executable
    """

    return os.access(path, os.X_OK) if path else False


def check_permission(path: str):
    """Check file or folder permission
    
    Arguments:
        path_folder {str} -- path folder or file
    
    Returns:
        bool -- if all stats were OK return true 

    """

    return all(
        (check_exists(path), check_is_readable(path), check_is_writable(path),
         check_is_executable(path))) if path else False

