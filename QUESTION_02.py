class Shape:
    def __init__(self, sides):
        self.sides = sides

    def display(self):
        if self.sides == 3:
            print("Triangle")
            

        elif self.sides == 4:
            print("Square")

        elif self.sides == 5:
            print("Pentagon")
        elif self.sides == 6:
            print("Hexagon")
        elif self.sides == 7:   
            print("Heptagon")
        elif self.sides == 8:
            print("Octagon")
        else:
            print("Shape not available")


for i in range(3):

    sides = int(input("Enter number of sides: "))

    shape1 = Shape(sides)

    print("Your Shape:")
    shape1.display()
    print()