from lab import Circle, Rectangle, Square, Triangle
c = Circle("Red", 5, True)
r = Rectangle("Blue", 4, 6, False)
s = Square("Green", 3, True)
t = Triangle("Yellow", 8, 6, True)
def sum_filled_area(shapes):
    total_area = 0
    for shape in shapes:
        if shape.filled:
            total_area += shape.area()
    return total_area
print (sum_filled_area([c, r, s, t]))