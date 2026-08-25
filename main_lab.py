from lab import Circle, Rectangle, Square, Triangle

print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:

    color = input("Enter color: ")
    radius = float(input("Enter radius: "))

    filled = input("Is it filled? (yes or no): ")

    if filled == "yes":
        filled = True
    else:
        filled = False

    c = Circle(color, radius, filled)
    c.show_info()

elif choice == 2:

    color = input("Enter color: ")
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    filled = input("Is it filled? (yes/no): ")

    if filled == "yes":
        filled = True
    else:
        filled = False

    r = Rectangle(color, length, breadth, filled)
    r.show_info()

elif choice == 3:

    color = input("Enter color: ")
    side = float(input("Enter side length: "))

    filled = input("Is it filled? (yes/no): ")

    if filled == "yes":
        filled = True
    else:
        filled = False

    s = Square(color, side, filled)
    s.show_info()

elif choice == 4:

    color = input("Enter color: ")
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    filled = input("Is it filled? (yes/no): ")

    if filled == "yes":
        filled = True
    else:
        filled = False

    t = Triangle(color, base, height, filled)
    t.show_info()


else:
    print("Invalid choice")
