from typing import Generator
import os
import sys


# assert to exists file tests
path_exists = [("tests/assets/file.txt", True),
               ("tests/assets/NOEXISTS", False), (None, False)]


# assert to permission file tests
path_allowed_access = []
path_allowed_access.extend(path_exists)
path_allowed_access.append(("tests/assets/file-nopermission.txt", False))

# assert to exists directory tests
directory_exists = [("tests/assets/foo/", True),
                    ("tests/assets/NOEXISTS/", False), (None, False)]


# assert test_get_files
generator_exists = [("tests/assets/foo/", True), ("tests/assets/NOEXISTS", True), (None, True)]

# assert test_get_files_extensions
expected_extensions = {'txt', 'mp4', 'odt', 'mp3'}


# test_delete_directory
directory_delete = [("tests/assets/foo/bar2/", True),
                    ("tests/assets/NOEXISTS/", False), (None, False)]

# test_create_directory
directory_create = [("tests/assets/foo/bar4/", True),
                    ("tests/assets/foo/bar3/", False),
                    (None, False)]

# test_move_directory and test_copy_directory
directory_move = [
    ("tests/assets/foo/bar3/", "tests/assets/bar3/", True),
    (None, None, False),
    ("tests/assets/foo/bar3/", None, False),
    (None, "tests/assets/foo/bar3/", False)]

# test_copy_file
copy_file = [("tests/assets/foo/empty.mp3", "tests/assets/empty.mp3", True),
                  (None, None, False), ("tests/assets/foo/empty.mp3", None, False),
                  (None, "tests/assets/foo/empty.mp3", False)]


# test_gen_random_bit_number
gen_bit_number = [(256, True), (1, True), (0, True), (-1, True), ("aa", True)]

# test_gen_hash
get_hash = [("test hash", 64), ("", 0), (0, 64)]

# test_sanitize_path
sanitize_path = [
    ("/home/ivan/Documents/test/", "/home/ivan/Documents/test"), 
    ("/home/ivan/Documents/test", "/home/ivan/Documents/test"), 
    ("", ""), 
    (0, None),
    (25, None)
]

# test_copy_to_temp_directory
copy_to_temp_dir = [("tests/assets/foo", True), (None, False)]

