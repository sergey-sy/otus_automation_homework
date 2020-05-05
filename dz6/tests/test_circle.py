from main import MyCircle


def test_name():
    circle_1 = MyCircle(10)
    assert circle_1.name == 'circle'


def test_area():
    circle_1 = MyCircle(10)
    assert circle_1.area == 314.1592653589793


def test_angles():
    circle_1 = MyCircle(10)
    assert circle_1.angles == 0


def test_perimeter():
    circle_1 = MyCircle(10)
    assert circle_1.perimeter == 62.83185307179586


def test_add_square():
    circle_1 = MyCircle(10)
    circle_2 = MyCircle(0.1)
    assert circle_1.add_square(circle_2) == 314.1906812855152
