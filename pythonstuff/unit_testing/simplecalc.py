from math import log10, floor


class SimpleCalc():
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    # def add(self):
    #     return self.num1 + self.num2
    #
    # def subtract(self):
    #     return self.num1 - self.num2
    #
    # def multiply(self):
    #     return self.num1 * self.num2
    #
    # def divide(self):
    #     return self.num1 / self.num2

    def add(self, num1, num2):
        return round(num1 + num2, 6)

    def subtract(self, num1, num2):
        return round(num1 - num2, 6)

    def multiply(self, num1, num2):
        # return round(num1 * num2, 3 * -int(floor(log10(abs(num1 * num2)))))
        return round(num1 * num2, 6)

    def divide(self, num1, num2):
        # return round(num1 / num2, 3 * -int(floor(log10(abs(num1 / num2)))))
        try:
            return round(num1 / num2, 6)
        except ZeroDivisionError:
            return ZeroDivisionError

