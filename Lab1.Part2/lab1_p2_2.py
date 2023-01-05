import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, numerator: int):
        if not isinstance(numerator, int):
            raise TypeError('It must be integer value')
        self.__numerator = numerator

    @denominator.setter
    def denominator(self, denominator: int):
        if not isinstance(denominator, int):
            raise TypeError('It must be integer value')
        if denominator == 0:
            raise ValueError('Division by zero is forbidden')
        self.__denominator = denominator

    def __str__(self):
        common_divisor = math.gcd(self.__numerator, self.__denominator)
        return f"{self.__numerator // common_divisor} / {self.__denominator // common_divisor}"

    def float_form(self):
        return self.__numerator / self.__denominator

division = Rational(6, 8)
print(division)
print(division.float_form())