#!/usr/bin/python

class Shape:
    def __init__(self):
        # default color
        self.color = 'black'

class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self)
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

if __name__ == '__main__':
    square = Square(4)
    print("color = {}".format(square.color))
    print("perimeter = {}".format(square.perimeter()))
    print("area = {}".format(square.area()))
