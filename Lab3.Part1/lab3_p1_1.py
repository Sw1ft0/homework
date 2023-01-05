import math


class Rational:

    def __init__(self, number_1=1, number_2=1):
        self.number_1 = number_1
        self.number_2 = number_2
        self.reduce()

    @property
    def number_1(self):
        return self.__number_1

    @property
    def number_2(self):
        return self.__number_2

    @number_1.setter
    def number_1(self, number_1: int):
        if not isinstance(number_1, int):
            raise TypeError('It must be integer value')
        self.__number_1 = number_1

    @number_2.setter
    def number_2(self, number_2: int):
        if not isinstance(number_2, int):
            raise TypeError('It must be integer value')
        self.__number_2 = number_2

    def reduce(self):
        if self.__number_2 == 0:
            raise ValueError('Division by zero is forbidden')
        gcd = math.gcd(self.number_1, self.number_2)
        self.number_1 = self.number_1 // gcd
        self.number_2 = self.number_2 // gcd
        return f"{self.__number_1} / {self.__number_2}"

    def __str__(self):
        return f"{self.__number_1}/{self.__number_2}"

    def float_form(self):
        return self.__number_1 / self.__number_2

    def __add__(self, other):
        num = self.number_1 * other.number_2 + self.number_2 * other.number_1
        den = self.number_2 * other.number_2
        return Rational(num, den)

    def __sub__(self, other):
        num = self.number_1 * other.number_2 - self.number_2 * other.number_1
        den = self.number_2 * other.number_2
        return Rational(num, den)

    def __mul__(self, other):
        num = self.number_1 * other.number_1
        den = self.number_2 * other.number_2
        return Rational(num, den)

    def __truediv__(self, other):
        num = self.number_1 * other.number_2
        den = self.number_2 * other.number_1
        return Rational(num, den)

    def __eq__(self, other):
        return self.number_1 == other.number_1 and self.number_2 == other.number_2

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.float_form() < other.float_form()

    def __gt__(self, other):
        return self.float_form() > other.float_form()


rational_number_1 = Rational(6, 8)
rational_number_2 = Rational(2, 4)
print(rational_number_1 > rational_number_2)
print(rational_number_1.float_form())