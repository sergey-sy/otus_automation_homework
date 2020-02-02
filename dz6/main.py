import Geometry


class MyGeometricalShape:
    def __init__(self,name:str, area:float, angles:int, perimeter:float):
        self.name = name
        self.area = area
        self.angles = angles
        self.perimeter = perimeter

    def add_square(self, figure) -> float:
        """Sum areas of two figures"""
        if isinstance(figure, MyGeometricalShape):
            return self.area + figure.area
        else:
             raise TypeError('Argument for add_square must be instance of MyGeometricalShape')


class MyTriangle(MyGeometricalShape):
    """
    Create triangle with 3 points. Each point have x, y, z.
    # >>> MyTriangle((0, 10, 0), (10, 0, 0), (0, 0, 0))
    """
    def __init__(self, x, y, z):
        _triangle = Geometry.Triangle(x, y, z)
        _perimeter = sum([x.length for x in _triangle.sides]) # Geometry - was forgotten realise _triangle.perimeter
        super().__init__(name='triangle',
                         area=_triangle.area,
                         angles=3,
                         perimeter=_perimeter
                         )


class MyCircle(MyGeometricalShape):
    """
    Create Circle with radius.
    >>> circle_1 = MyCircle(10)
    """
    def __init__(self, radius):
        _circle = Geometry.Circle(center=None, radius=radius)
        super().__init__(name='circle',
                         area=_circle.area,
                         angles=0,
                         perimeter=_circle.circumfrence
                         )


class MyRectangle(MyGeometricalShape):
    def __init__(self, width, height):
        _rectangle = Geometry.Rectangle(origin=None, width=width, height=height)
        super().__init__(name='rectangle',
                         area=_rectangle.area,
                         angles=4,
                         perimeter=_rectangle.perimeter
                         )


class MySquare(MyRectangle):
    def __init__(self, width):
        super().__init__(width, height=width)
        self.name = 'square'


def main():

    triangle_1 = MyTriangle((0, 10, 0), (10, 0, 0), (0, 0, 0))
    triangle_2 = MyTriangle((0, 20, 0), (10, 0, 0), (0, 0, 0))
    print(triangle_1.name)
    print(triangle_1.area)
    print(triangle_1.angles)
    print(triangle_1.perimeter)
    print()
    print(triangle_2.name)
    print(triangle_2.area)
    print(triangle_2.angles)
    print(triangle_2.perimeter)
    print()
    print(triangle_1.add_square(triangle_2))

    circle_1 = MyCircle(10)
    print(circle_1.area)
    print(circle_1.perimeter)
    print(circle_1.add_square(triangle_1))
    print()
    rectangle_1 = MyRectangle(2, 4)
    print(rectangle_1.name)
    print(rectangle_1.area)
    print(rectangle_1.angles)
    print(rectangle_1.perimeter)
    print()
    square_1 = MySquare(2)
    print(square_1.name)
    print(square_1.area)
    print(square_1.angles)
    print(square_1.perimeter)
    print(triangle_1.add_square(square_1))
    print()
    params = [
        [(0, 10, 0), (10, 0, 0), (10, 10, 10)],
        [(0, 20, 0), (10, 0, 0), (0, 0, 0)],
        [(0, 10, 0), (10, 0, 0), (0, 0, 30)],
        [(15, 0, 0), (0, 15, 0), (0, 0, 15)],
        [(0, 25, 0), (15, 0, 0), (0, 0, 15)]
    ]

    for i in params:
        _tr = MyTriangle(*i)
        print(_tr.perimeter)


if __name__ == '__main__':
    main()