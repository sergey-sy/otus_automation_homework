from main import MyRectangle


def test_name():
    rectangle_1 = MyRectangle(2, 4)
    assert rectangle_1.name == 'rectangle'


def test_area():
    rectangle_1 = MyRectangle(2, 4)
    assert rectangle_1.area == 8.0


def test_angles():
    rectangle_1 = MyRectangle(2, 4)
    assert rectangle_1.angles == 4


def test_perimeter():
    rectangle_1 = MyRectangle(2, 4)
    assert rectangle_1.perimeter == 12.0


def test_add_square():
    rectangle_1 = MyRectangle(2, 4)
    rectangle_2 = MyRectangle(3, 5)
    assert rectangle_2.add_square(rectangle_1) == 23.0
