import os
import shutil
import tempfile

def move_directory(dir_src: str, dir_dst: str) -> bool:
    """move directories
    
    Arguments:
        dir_src {str} -- source directory
        dir_dst {str} -- destination directory
    
    Returns:
        bool -- return True if successful
    """

    if not dir_src or not dir_dst:
        return False

    if not os.path.exists(dir_src):
        print(f"dir_src not found. dir_src: {dir_src}")
        return False

    try:
        shutil.move(dir_src, dir_dst)

    except OSError as error:
        print(error)
        return False

    return True


def copy_directory(path_src: str, path_dst: str):
    """copy directory
    
    Arguments:
        path_src {str} -- copy source directory
        path_dst {str} -- copy destination directory 
    
     """

    if not path_src or not path_dst:
        print(f"path_src could be empty. path_src: {path_src}")
        print(f"path_dst could be empty. path_dst: {path_dst}")
        return False

    for item in os.listdir(path_src):
        src = os.path.join(path_src, item)
        dst = os.path.join(path_dst, item)

        if os.path.isdir(src):
            shutil.copytree(src, dst, symlinks=False, ignore=None)

        else:
            shutil.copy2(src, dst)

    return True
    

def delete_directory(path)-> True:
    """delete directory
    
    Arguments:
        path {str} -- path to directory
    
    Returns:
        True -- return if successful
    """

    if not path or not os.path.exists(path):
        return False

    return shutil.rmtree(path, ignore_errors=True)


def create_directory(path: str, recursive=False)-> True:
    """create directory
    
    Arguments:
        path {str} -- path to create a new directory
    
    Keyword Arguments:
        recursive {bool} -- create directories recursive (default: {False})
    
    Returns:
        True -- if successful returns True
    """

    if not path:
        return False

    try:
        if recursive:
            os.makedirs(path)
        else:
            os.mkdir(path)
    except IOError as error:
        print(error)
        return False
    return True


def get_currrent_directory()-> str:
    """get current directory
    
    Returns:
        str -- current directory
    """

    return os.getcwd()


def set_current_directory(directory: str)-> True:
    """set current directory
    
    Arguments:
        directory {str} -- directory path
    
    Returns:
        True -- return True if successful
    """
    if not directory:
        return False

    if not os.path.exists(directory):
        return False

    os.chdir(directory)

    return True


def get_temp_directory():
    """get OS temporary directory

    Returns:
        str -- temporary directory
    """

    return tempfile.gettempdir()


def copy_file(file_src: str, file_dst: str) -> bool:
    """copy file
    
    Arguments:
        file_src {str} -- source file
        file_dst {str} -- destination file

    Returns:
        bool -- Returns True if successful
    """

    if not file_src or not file_dst:
        print(f"file_src could be empty. file_src: {file_src}")
        print(f"file_dst could be empty. file_dst: {file_dst}")
        return False


    if not os.path.isfile(file_src):
        print(f"file_src not found. file_src: {file_src}")
        return False

    try:
        shutil.copyfile(file_src, file_dst)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        return False
    return True
