class Rectangle():
    def __init__(self, w=1.0, l=1.0):
        self.setter(w, l)

    def get_w(self):
        return self.width

    def get_l(self):
        return self.length
    
    def setter(self, w, l):
        if isinstance(w, float) and isinstance(l, float):
            if 0<w<20.0 and 0<l<20.0:
                self.width  = w
                self.length = l
            else:
                raise ValueError("Values must be 0<x<20")
        else:
            raise TypeError("It must be float numbers")

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

figure = Rectangle(0, 4.0)
print('Rectangle area -> ', figure.area())
print('Rectangle perimeter -> ', figure.perimeter())
figure.setter(7.0, 5.0)
print('Rectangle area -> ', figure.area())
print('Rectangle perimeter -> ', figure.perimeter())
