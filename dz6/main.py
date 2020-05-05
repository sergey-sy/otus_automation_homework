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
    >>> MyTriangle((0, 10, 0), (10, 0, 0), (0, 0, 0))
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
    """
    Create Rectangle by sides.
    >>> rectangle_1 = MyRectangle(2, 4)
    """
    def __init__(self, width, height):
        _rectangle = Geometry.Rectangle(origin=None, width=width, height=height)
        super().__init__(name='rectangle',
                         area=_rectangle.area,
                         angles=4,
                         perimeter=_rectangle.perimeter
                         )


class MySquare(MyRectangle):
    """
    Create Square by side.
    >>> square_1 = MySquare(2)
    """
    def __init__(self, width):
        super().__init__(width, height=width)
        self.name = 'square'
