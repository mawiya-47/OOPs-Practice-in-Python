from lab import Circle, Rectangle, Square, Triangle

total = 0
circle = 0
rectangle = 0
square = 0
triangle = 0
filled = 0
unfilled = 0


while True:

    print("\n1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Triangle")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    if choice == 1:

        color = input("Enter color: ")
        radius = float(input("Enter radius: "))
        f = input("Filled? yes/no: ")

        if f == "yes":
            f = True
        else:
            f = False

        obj = Circle(color, radius, f)
        circle = circle + 1

    elif choice == 2:

        color = input("Enter color: ")
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        f = input("Filled? yes/no: ")

        if f == "yes":
            f = True
        else:
            f = False

        obj = Rectangle(color, length, breadth, f)
        rectangle = rectangle + 1

    elif choice == 3:

        color = input("Enter color: ")
        side = float(input("Enter side: "))
        f = input("Filled? yes/no: ")

        if f == "yes":
            f = True
        else:
            f = False

        obj = Square(color, side, f)
        square = square + 1

    elif choice == 4:

        color = input("Enter color: ")
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        f = input("Filled? yes/no: ")

        if f == "yes":
            f = True
        else:
            f = False

        obj = Triangle(color, base, height, f)
        triangle = triangle + 1

    else:
        print("Wrong choice")
        continue

    total = total + 1

    if f == True:
        filled = filled + 1
    else:
        unfilled = unfilled + 1

    obj.show_info()


print("\n===== SUMMARY =====")

print("Total Shapes:", total)
print("Total Circle:", circle)
print("Total Square:", square)
print("Total Triangle:", triangle)
print("Total Rectangle:", rectangle)
print("Total Filled:", filled)
print("Total Unfilled:", unfilled)