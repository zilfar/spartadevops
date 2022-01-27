# PyTest
from quadrilateral import Rectangle, Square


def test_rectangle_perimeter():
    assert Rectangle(10, 8).perimeter() == 36
    assert Rectangle(4.8, 9.8).perimeter() == 29.2
    assert Rectangle(0, 4).perimeter() != float or int
    assert Rectangle(-5, -8).perimeter() != float or int


def test_square_perimeter():
    assert Square(4).perimeter() == 16
    assert Square(4.2).perimeter() == 16.8
    assert Square(-9).perimeter() != float or int
    assert Square(0).perimeter() != float or int


def test_rectangle_area():
    assert Rectangle(10, 8).area() == 80
    assert Rectangle(4.8, 9.8).area() == 47.04
    assert Rectangle(0, 4).area() != float or int
    assert Rectangle(-5, -8).area() != float or int


def test_square_area():
    assert Square(4).area() == 16
    assert Square(4.2).area() == 17.64
    assert type(Square(0).area()) == int or type(Square(0).area()) == float
    assert type(Square(-5).area()) == int or type(Square(-5).area()) == float
    assert type(Square(-5).area()) != int


def test_square_enclosure():
    assert Square(8).get_number_enclosing(Square(4)) == 4
    assert Square(4).get_number_enclosing(Square(4)) == 1
    assert Square(4).get_number_enclosing(Square(3)) == 1
    assert Square(4).get_number_enclosing(Square(6)) == 0
    assert Square(28).get_number_enclosing(Square(16)) == 1


def test_square_reprstr():
    assert repr(Square(20)) == f"Square(length={Square(20).length})"
    assert Square(20).__str__() == f"This is a Square with length size: {Square(20).length}."


def test_set_length_width():
    new_square = Square(40)
    new_square.setLength(20)
    assert new_square.length == 20
    new_square.setLength(80)
    assert new_square.length == 80
    new_rectangle = Rectangle(20, 60)
    new_rectangle.setWidth(40)
    assert new_rectangle.width == 40
    new_rectangle.setLength(90)
    assert new_rectangle.length == 90


