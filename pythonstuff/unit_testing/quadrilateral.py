from math import floor


class Rectangle:
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def perimeter(self):
        return abs(round(self.width * 2 + self.length * 2, 6))
    
    def area(self):
        return round(self.width * self.length, 6)

    def setWidth(self, new_width):
        self.width = float(new_width)

    def setLength(self, new_length):
        self.length = float(new_length)

    def __str__(self):
        return f"This is a Rectangle with length size: {self.length} and width size: {self.width}."

    def __repr__(self):
        return f"Rectangle(length={self.length})"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.length = float(length)

    def get_number_enclosing(self, square):
        return int(self.length / square.length) ** 2

    def setWidth(self, dimension):
        self.length = float(dimension)

    def setLength(self, dimension):
        self.length = float(dimension)

    def __str__(self):
        return f"This is a Square with length size: {self.length}."

    def __repr__(self):
        return f"Square(length={self.length})"

# square1 = Square(4)
# print(square1)
# print(Square(4).length)
# print(Square(20))