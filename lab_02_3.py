x = 100

print("Integer Example")
print("---------------------------")
print("Value of x:", x)
print("Address of x (Decimal):", id(x))
print("Address of x (Hex):", hex(id(x)))

print()

# List Example
a = [10, 20, 30]
b = a              
c = [10, 20, 30]   

print("List Example")
print("---------------------------")
print("Address of a:", hex(id(a)))
print("Address of b:", hex(id(b)))
print("Address of c:", hex(id(c)))

print()

print("Comparison")
print("---------------------------")
print("a and b have same address:", id(a) == id(b))
print("a and c have same address:", id(a) == id(c))

print()

# String Example
name1 = "Muhammad Mawiya"
name2 = name1

print("String Example")
print("---------------------------")
print("Address of name1:", hex(id(name1)))
print("Address of name2:", hex(id(name2)))
print("Same Address:", id(name1) == id(name2))