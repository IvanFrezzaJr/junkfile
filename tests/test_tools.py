import pytest
import os
from junkfile import tools
from tests import testdata

@pytest.mark.parametrize("test_input, expected_input",
                         testdata.directory_exists)
def test_set_currrent_directory(test_input, expected_input):
    # get current directory
    current_directory = os.getcwd()

    # make asserts
    result = tools.set_current_directory(test_input)
    assert result == expected_input, "If exists, could be returned True instead False"

    # return to current directory
    tools.set_current_directory(current_directory)


@pytest.mark.parametrize("test_input, expected_input",
                         testdata.directory_delete)
def _test_delete_directory(test_input, expected_input):
    result = tools.delete_directory(test_input)
    assert result == expected_input, f"Returns {result} instead {result}"

    # recreate directory
    tools.create_directory(testdata.directory_delete[0][0])


@pytest.mark.parametrize("test_input, expected_input",
                         testdata.directory_create)
def test_create_directory(test_input, expected_input):
    result = tools.create_directory(test_input)
    assert result == expected_input, f"Returns {result} instead {expected_input}"

    tools.delete_directory(testdata.directory_create[0][0])


@pytest.mark.parametrize("test_input1, test_input2, expected_input",
                         testdata.directory_move)
def test_move_directory(test_input1, test_input2, expected_input):
    result = tools.move_directory(test_input1, test_input2)
    assert result == expected_input, f"Returns {result} instead {expected_input}"

    tools.move_directory(test_input2, test_input1)


@pytest.mark.parametrize("test_input1, test_input2, expected_input",
                         testdata.directory_move)
def test_copy_directory(test_input1, test_input2, expected_input):
    result = tools.copy_directory(test_input1, test_input2)
    assert result == expected_input, f"Returns {result} instead {expected_input}"


@pytest.mark.parametrize("test_input1, test_input2, expected_input",
                         testdata.copy_file)
def test_copy_file(test_input1, test_input2, expected_input):
    result = tools.copy_file(test_input1, test_input2)
    assert result == expected_input, f"Returns {result} instead {expected_input}"

    if test_input1 and test_input2:
        tools.copy_file(test_input2, test_input1)
        os.remove(test_input2)
