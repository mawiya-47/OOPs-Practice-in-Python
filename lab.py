import math
class Shape:
    def __init__(self, color, filled=False):
        self.color = color
        self.filled = filled

    def fill_color(self):
        self.filled = True

    def show_info(self):
        print("Color:", self.color)
        print("Filled:", self.filled)


class Circle(Shape):

    def __init__(self, color, radius, filled=False):
        super().__init__(color, filled)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def show_info(self):
        super().show_info()
        print("Radius:", self.radius)
        print("Area:", self.area())


class Rectangle(Shape):

    def __init__(self, color, length, breadth, filled=False):
        super().__init__(color, filled)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def show_info(self):
        super().show_info()
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.area())


class Square(Shape):

    def __init__(self, color, side, filled=False):
        super().__init__(color, filled)
        self.side = side

    def area(self):
        return self.side ** 2

    def show_info(self):
        super().show_info()
        print("Side:", self.side)
        print("Area:", self.area())


class Triangle(Shape):

    def __init__(self, color, base, height, filled=False):
        super().__init__(color, filled)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def show_info(self):
        super().show_info()
        print("Base:", self.base)
        print("Height:", self.height)
        print("Area:", self.area())