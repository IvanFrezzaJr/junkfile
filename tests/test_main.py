import pytest
import os
import tempfile
import shutil
import datetime
import glob
from junkfile import main
from typing import Generator
from tests import testdata

@pytest.mark.parametrize("test_input, expected_input",
                         testdata.get_hash)
def test_gen_hash(test_input, expected_input):
    result = main.get_hash(test_input)
    size = len(result)
    assert size == expected_input


@pytest.mark.parametrize("test_input, expected_input",
                         testdata.gen_bit_number)
def test_gen_random_bit_number(test_input, expected_input):
    result = main.gen_random_bit_number(test_input)
    is_number = isinstance(result, int)
    assert is_number == expected_input

    
@pytest.mark.parametrize("test_input, expected_input",
                         testdata.generator_exists)
def test_get_files(test_input, expected_input):
    gen = main.get_files(test_input)
    result = isinstance(gen, Generator)
    assert result == expected_input, f"Returns True if is a generator instead {result}"


@pytest.mark.parametrize("test_input, expected_input",
                         testdata.sanitize_path)
def test_sanitize_path(test_input, expected_input):
    result = main.sanitize_path(test_input)
    assert result == expected_input, f"Returns True if is a generator instead {result}"


def test_get_blacklist_directories():
    result = main.get_blacklist_directories()
    assert isinstance(result, list) == True


def test_copy_to_temp_directory():
    
    param1 = "tests/assets/foo"
    path_expected = tempfile.gettempdir()

    result = main.copy_to_temp_directory(param1)
    path_result = os.path.dirname(result)
    folder_result = os.path.basename(result)

    assert path_result == path_expected, f"Returns {path_result} instead {path_expected}"
    assert len(folder_result) == 64, f"Returns len {len(folder_result)} instead 64"

    if os.path.exists(result):
        shutil.rmtree(result)

    param2 = ""
    result = main.copy_to_temp_directory(param2)
    assert result == None 

    param2 = 24
    result = main.copy_to_temp_directory(param2)
    assert result == None

    
def test_copy_to_organized_directory():
    src_dir = "tests/assets/foo/"
    dest_dir = "tests/assets/foo2/"
    result = main.copy_to_organized_directory(src_dir, dest_dir)
    assert result == True

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        os.mkdir(dest_dir)

    src_dir = ""
    dest_dir = ""
    with pytest.raises(OSError):
        result = main.copy_to_organized_directory(src_dir, dest_dir)

    src_dir = "tests/assets/foo"
    dest_dir = ""
    with pytest.raises(IOError):
        result = main.copy_to_organized_directory(src_dir, dest_dir)
    
    src_dir = ""
    dest_dir = "tests/assets/foo_organized"
    with pytest.raises(IOError):
        result = main.copy_to_organized_directory(src_dir, dest_dir)
    

def test_current_directory_handler():
    changed_dir = "tests/assets/foo"
    current_dir = os.getcwd()

    with main.current_directory_handler(changed_dir):
        pass

    new_current_dir = os.getcwd()
    assert current_dir == new_current_dir

    changed_dir = ""
    with pytest.raises(ValueError):
        with main.current_directory_handler(changed_dir):
            pass
    

def test_build_directory_path_with_date():
    date_dir = "tests/assets/foo"
    result = main.build_directory_path_with_date(date_dir)

    splited_result = result.split("-", 2)

    assert splited_result[0] == date_dir

    assert splited_result[1] == "jk"

    date_string, _ = splited_result[2].split(".")
    date_format = '%Y-%m-%d %H:%M:%S'
    date_obj = datetime.datetime.strptime(date_string, date_format)

    assert isinstance(date_obj, datetime.date) == True

    date_dir = ""
    result = main.build_directory_path_with_date(date_dir)
    assert result == None
    
