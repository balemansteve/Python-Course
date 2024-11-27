from math import pi


class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def area(shape):
    print(f"{shape.area()}")

circle = Circle(5)

rectangle = Rectangle(5, 10)

area(circle)
area(rectangle)