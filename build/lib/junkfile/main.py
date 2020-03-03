import os
import re
import shutil
import random
import stat
import platform
import hashlib
import argparse
import contextlib
from typing import Generator
from pathlib import Path
from datetime import datetime
import checks
import tools


def get_files(directory: str) -> Generator:
    """get list files from directory
    
    Arguments:
        directory {str} -- directory path
    
    Returns:
        Generator -- generator 
    
    Yields:
        Generator -- file generator
    """

    if not directory or not os.path.exists(directory):
        print(f"directory not found. directory: {directory}")
        return None

    dirAbs = os.path.abspath(directory)
    
    for root, _, files in os.walk(dirAbs):
        for name in files:
            yield os.path.join(root, name)


def get_hash(string_=""):
    """get random hash
    
    Returns:
        str -- get hash
    """

    string_ = str(string_)

    if not string_:
        return ""

    return hashlib.sha256(str(
        string_).encode('utf-8')).hexdigest()

def gen_random_bit_number(number_bits=1):
    if isinstance(number_bits, int) and number_bits > 0:
        return random.getrandbits(number_bits)
    return 0


def sanitize_path(path: str) -> str:
    """sanitize path
    
    remove last slash at end of the 
    """
    removeLastSlash = slice(0, -1)
    return path if not path.endswith("/") else path[removeLastSlash]

def get_blacklist_directories():
    """list of OS directories
    
    """
    return ["c:/", "d:/", "/", "/bin", "/etc",
            "/lib", "/lib64", "/run", "/sbin",
            "/sys", "/proc", "/root", "/srv",
            "/usr"]


def copy_to_temp_directory(path_folder: str) -> str:
    """copy directory to OS temp directory
    
    Arguments:
        path_folder {str} -- directory path
    
    Returns:
        str -- temp directory path
    """

    random_number = gen_random_bit_number(256)

    # generate hash for temp folder
    hash_folder = get_hash(random_number)

    # get os temp directory
    temp_dir = tools.get_temp_directory()

    # create temp directory
    temp_dir = os.path.join(temp_dir, hash_folder)

    try:
        # create directory
        tools.create_directory(temp_dir)

        # copy directory to OS temp directory
        tools.copy_directory(path_folder, temp_dir)

    except IOError as error:
        print(error)
        return False
    return temp_dir


def copy_to_organized_directory(dir_src: str, dir_dst: str) -> bool:
    """copy source directory to organized directory

    Get content from source directory and copy to a new directory
    into new folders with the extentions name 
    
    Arguments:
        dir_src {str} -- source directory
        dir_dst {str} -- destination directory
    
    Raises:
        IOError: path dir_src not found
        IOError: path dir_dst not found
    
    Returns:
        bool -- if successful return True
    """

    if not checks.check_exists(dir_src):
        raise IOError("Directory '{0}' not found.".format(dir_src))

    if not checks.check_exists(dir_dst):
        raise IOError("Directory '{0}' not found.".format(dir_dst))
     

    # copy files temp to new directory
    list_files = get_files(dir_src)

    for file in list_files:
        basename = os.path.basename(file)
        search = re.search(r"\.([A-Za-z0-9]+)$", basename)

        if search:
            extension = search.group(1)
            # check = [ext for ext in extensions if search.group(1) == ext]

            
            directory_extension = os.path.join(dir_dst, extension)

            if not checks.check_exists(directory_extension):
                tools.create_directory(directory_extension)

            # build target directory
            target_directory = os.path.join(directory_extension, basename)

            # copy file
            tools.copy_file(file, target_directory)

    return True


@contextlib.contextmanager
def current_directory_handler(dir_dst: str):
    """context directory manager

    manager context directory. Get current directory and set after operation ends:

    usage:
        with current_directory_handler("")

    Arguments:
        dir_dst {str} -- directory to set
    
    Raises:
        Exception: if User don't have permition to read the directory
    """

    if not checks.check_permission(dir_dst):
        raise Exception("You don't have permition to access that folder: {0}".format(dir_dst))

    # get current directory
    current_dir = tools.get_currrent_directory()

    # set target directory
    tools.set_current_directory(dir_dst)

    yield

    # set current directory
    tools.set_current_directory(current_dir)
    

def build_directory_path_with_date(path_folder: str) -> str:
    """make a new directory path
    
    Arguments:
        path_folder {str} -- path folder
     
    Returns:
        str -- return new name path
    """

    path_folder = sanitize_path(path_folder)

    folder_name = os.path.basename(path_folder)

    # check if will copy
    made_path = os.path.join(
        os.path.dirname(path_folder),
        folder_name + "-jk-" + str(datetime.now()))
    
    return made_path


def run(path_folder, create_copy=True):
    """main script run 
    
    Arguments:
        path_folder {str} -- folder to organize
    
    Keyword Arguments:
        create_copy {bool} -- create a folder copy (default: {True})
    
    Raises:
        IOError: if folder doesn't exists
    """

    print(f"\n[Junkfile] - Parameters: ")
    print(f"[Junkfile] -   path_folder: {path_folder}")
    print(f"[Junkfile] -   create_copy: {create_copy}\n")
    print("[Junkfile] - executing...")
    
    # check if path exits
    if not checks.check_exists(path_folder):
        raise Exception("Please choose a directory.")
        
    # check if is not inthe blacklist directory
    if path_folder in get_blacklist_directories():
        raise Exception("Directory may not be selected. Try another directory")
    
    # remove last slash
    path_folder = sanitize_path(path=path_folder)

    '''directory contextmanager

    check if path has permission to change, set as current directory and
    change to old current directory at the end

    '''
    with current_directory_handler(path_folder):

        # copy folder to to OS temp directory
        temp_dir = copy_to_temp_directory(path_folder=path_folder)

        # make path
        new_directory = build_directory_path_with_date(path_folder=path_folder)

        # create a new folder
        if not tools.create_directory(new_directory):
            raise Exception(f"new_directory could not be created. new_directory: '{new_directory}'")
            
        # copy to new folder
        copy_to_organized_directory(dir_src=temp_dir, dir_dst=new_directory)

        # delete folders
        if checks.check_exists(temp_dir):
            tools.delete_directory(temp_dir)

        # check if is a copy
        if not create_copy:
            tools.delete_directory(path_folder)
            tools.move_directory(new_directory, path_folder)

    if create_copy:
        print(f"[Junkfile] -   Was created new directory: {new_directory}")
        
    print("[Junkfile] - executed!")

    return True

if "__main__" or __file__:
    test = get_hash()
    print(test)
    print(gen_random_bit_number(256))

    nm = 113168883980528996301509502268917513974659074941811986235425482721364707972667
    print(nm.bit_length())

    """
    hashlib.sha256(str(
        random.getrandbits(256)).encode('utf-8')).hexdigest()
    
    """