import math


class Shape:

    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * (self.x + self.y)


class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        p = (self.x + self.y + self.z) / 2
        return (p * (p - self.x) * (p - self.y) * (p - self.z)) ** 0.5

    def perimeter(self):
        return self.x + self.y + self.z


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)

    def perimeter(self):
        return 2 * math.pi * self.r


circle = Circle(5)
print("Circle area", circle.area())
print("Circle perimeter", circle.perimeter())
rectangle = Rectangle(5, 10)
print("Rectangle area", rectangle.area())
print("Rectangle perimeter", rectangle.perimeter())
triangle = Triangle(5, 10, 15)
print("Triangle area", triangle.area())
print("Triangle perimeter", triangle.perimeter())
shape = Shape()
print("Shape area", shape.area())
print("Shape perimeter", shape.perimeter())
