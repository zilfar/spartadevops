from math import floor


class Rectangle:
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def perimeter(self):
        return abs(round(self.width * 2 + self.length * 2, 6))
    
    def area(self):
        return round(self.width * self.length, 6)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.length = float(length)

    def get_number_enclosing(self, square):
        return floor(self.area() / square.area())
