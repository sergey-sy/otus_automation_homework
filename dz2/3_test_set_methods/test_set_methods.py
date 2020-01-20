import pytest


def test_discard():
    """Test the set.discard() method. Remove element elem from the set if it is present."""
    st = {1, 2, 3, 4}
    st.discard(4)
    assert st == {1, 2, 3}


def get_sets_kit():
    return [
            [{1, 2, 3}, {2, 3}],
            [{2, 3}, {2}],
            [{5, 6, 7, 8}, {5, 6, 7, 8}],
            [{1, 2, 3}, set()]
            ]


@pytest.fixture(params=get_sets_kit())
def fixture_with_params(request):
    return request.param


def test_issubset(fixture_with_params):
    """
    Test whether every element in the set is in other. set <= other
    """
    set_a, set_b = fixture_with_params
    assert set_b.issubset(set_a)
