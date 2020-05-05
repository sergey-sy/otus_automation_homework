import pytest

from main import MyTriangle


@pytest.mark.parametrize("x, y, z, expected",
                         [
                             ((0, 10, 0), (10, 0, 0), (10, 10, 10), 50.0),
                             ((0, 20, 0), (10, 0, 0), (0, 0, 0), 100.0),
                             ((0, 10, 0), (10, 0, 0), (0, 0, 30), 50.0),
                             ((15, 0, 0), (0, 15, 0), (0, 0, 15), 112.5),
                             ((0, 25, 0), (15, 0, 0), (0, 0, 15), 187.5)
                         ])
def test_area(x, y, z, expected):
    triangle = MyTriangle(x, y, z)
    assert triangle.area == expected


@pytest.mark.parametrize("x, y, z, expected",
                         [
                             ((0, 10, 0), (10, 0, 0), (10, 10, 10), 42.42640687119285),
                             ((0, 20, 0), (10, 0, 0), (0, 0, 0), 52.3606797749979),
                             ((0, 10, 0), (10, 0, 0), (0, 0, 30), 77.38768882709854),
                             ((15, 0, 0), (0, 15, 0), (0, 0, 15), 63.63961030678928),
                             ((0, 25, 0), (15, 0, 0), (0, 0, 15), 79.52272238404943)
                         ])
def test_perimeter(x, y, z, expected):
    triangle = MyTriangle(x, y, z)
    assert triangle.perimeter == expected


def test_add_square():
    triangle_1 = MyTriangle((0, 10, 0), (10, 0, 0), (10, 10, 10))
    triangle_2 = MyTriangle((0, 20, 0), (10, 0, 0), (0, 0, 0))
    assert triangle_1.add_square(triangle_2) == 150

def test_add_square_exception():
    triangle_1 = MyTriangle((0, 10, 0), (10, 0, 0), (10, 10, 10))
    try:
        triangle_1.add_square('string')
    except TypeError:
        assert True
    else:
        assert False

def test_angels():
    triangle_1 = MyTriangle((0, 10, 0), (10, 0, 0), (10, 10, 10))
    assert triangle_1.angles == 3

def test_name():
    triangle_1 = MyTriangle((0, 10, 0), (10, 0, 0), (10, 10, 10))
    assert triangle_1.name == 'triangle'
