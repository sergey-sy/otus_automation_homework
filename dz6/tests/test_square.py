from main import MySquare


def test_name():
    square_1 = MySquare(2)
    assert square_1.name == 'square'


def test_area():
    square_1 = MySquare(2)
    assert square_1.area == 4.0


def test_angles():
    square_1 = MySquare(2)
    assert square_1.angles == 4


def test_perimeter():
    square_1 = MySquare(2)
    assert square_1.perimeter == 8.0


def test_add_square():
    square_1 = MySquare(2)
    square_2 = MySquare(3)
    assert square_2.add_square(square_1) == 13.0
