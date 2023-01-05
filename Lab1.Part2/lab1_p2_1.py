class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, length):
        if not isinstance(length, float):
            raise TypeError("It must be float value")
        if 0.0 < length < 20.0:
            self.__length = length
        else:
            raise ValueError("Values must be 0<x<20")

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError("It must be float value")
        if 0.0 < width < 20.0:
            self.__width = width
        else:
            raise ValueError("Values must be 0<x<20")

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2*(self.__length + self.__width)

figure = Rectangle(3.0, 4.0)

print('Rectangle area -> ', figure.area())
print('Rectangle perimeter -> ', figure.perimeter())
figure.length = 7.0
figure.width = 5.0
print('Rectangle area -> ', figure.area())
print('Rectangle perimeter -> ', figure.perimeter())
