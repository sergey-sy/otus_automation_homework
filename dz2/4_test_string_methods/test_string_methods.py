import pytest


def test_capitalize():
    """
    Test the string.capitalaize() method which
    return a copy of the string with its first character capitalized and the rest lowercased.
    """

    str = 'hello'
    assert str.capitalize() == 'Hello'


@pytest.fixture(params=[(0, 0), (2, 6), (8, 12), (14, 18), (19, -1)])
def fixture_with_params(request):
    return request.param


def test_str_find(fixture_with_params):
    """
    Test test_string.find() which return the lowest index in the string where substring sub is found within the slice s[start:end].
    Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
    """

    test_string = 'PythonPythonPythonPython'

    start_index, return_index = fixture_with_params
    test_indx = test_string.find('P', start_index)
    assert test_indx == return_index
