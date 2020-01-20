import pytest


def test_append():
    """Test the list.append() method. Add element in list"""
    lst = [1, 2, 3]
    lst.append(4)
    assert lst == [1, 2, 3, 4]


@pytest.fixture(params=[1, 2, 3, 4])
def fixture_with_params(request):
    return request.param


def test_count(fixture_with_params):
    lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    assert lst.count(fixture_with_params) == fixture_with_params
