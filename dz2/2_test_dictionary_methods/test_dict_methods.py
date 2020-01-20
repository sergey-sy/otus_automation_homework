import pytest


@pytest.fixture
def get_dct_1():

    dct_1 = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four'
    }
    return dct_1


@pytest.fixture
def get_dct_2():
    dct_2 = {
        1: 'one',
        2: 'two',
        3: 'three'
    }
    return dct_2


def test_dict_copy(get_dct_1):
    """Test that dict.copy() return a shallow copy of the dictionary."""

    copy_dict = get_dct_1.copy()
    assert copy_dict == get_dct_1


def test_dict_items(get_dct_2):
    """Test that dict.items() return a new view of the dictionary’s items ((key, value) pairs)."""

    dict_pairs = [(key, value) for key, value in get_dct_2.items()]
    assert dict_pairs == [(1, 'one'), (2, 'two'), (3, 'three')]


class TestPop:
    """
    Test the dict.pop() method. If key is in the dictionary, remove it and return its value, else return default.
    If default is not given and key is not in the dictionary, a KeyError is raised.
    """

    def test_remove_and_return_value(self, get_dct_1, get_dct_2):
        """If key is in the dictionary, remove it and return its value."""

        dct_1 = get_dct_1
        dct_2 = get_dct_2
        pop_value = dct_1.pop(4)
        assert dct_1 == dct_2 and pop_value == 'four'

    def test_try_remove_nonexistent_key_and_return_default(self, get_dct_2):
        """If key is in the dictionary, remove it and return its value, else return default."""

        dct_2 = get_dct_2
        dct_3 = dct_2.copy()
        pop_value = dct_2.pop(5, 'default_value')
        assert dct_2 == dct_3 and pop_value == 'default_value'

    def test_try_remove_and_and_get_key_error(self, get_dct_2):
        """If default is not given and key is not in the dictionary, a KeyError is raised."""

        with pytest.raises(KeyError):
            get_dct_2.pop(5)
