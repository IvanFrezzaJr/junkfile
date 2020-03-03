import pytest
import os
from junkfile import checks
from tests import testdata

@pytest.mark.parametrize("test_input, expected_input", testdata.path_exists)
def test_check_exists(test_input, expected_input):
    result = checks.check_exists(test_input)
    assert result == expected_input, "If exists, could be returned True instead False"


@pytest.mark.parametrize("test_input, expected_input",
                         testdata.path_allowed_access)
def test_check_is_readable(test_input, expected_input):
    result = checks.check_is_readable(test_input)
    assert result == expected_input, "If exists, could be returned True instead False"


@pytest.mark.parametrize("test_input, expected_input",
                         testdata.path_allowed_access)
def test_check_is_writable(test_input, expected_input):
    result = checks.check_is_writable(test_input)
    assert result == expected_input, "If exists, could be returned True instead False"


@pytest.mark.parametrize("test_input, expected_input",
                         testdata.path_allowed_access)
def test_check_is_executable(test_input, expected_input):
    result = checks.check_is_executable(test_input)
    assert result == expected_input, "If exists, could be returned True instead False"


@pytest.mark.parametrize("test_input, expected_input", testdata.path_allowed_access)
def test_check_permission(test_input, expected_input):
    result = checks.check_permission(test_input)
    assert result == expected_input, "If exists, could be returned True instead False"

