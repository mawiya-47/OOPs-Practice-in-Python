while True:
    n = int(input("Enter rows (1-9): "))
    if n <= 9 and n > 0:
        break
    print("Invalid input")

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    
    for j in range(n - i):
        print(" ", end="")
    
    for j in range(1, i + 1):
        print(j, end="")
    
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

for i in range(n - 1, 0, -1):
    
    for j in range(n - i):
        print(" ", end="")
    
    for j in range(1, i + 1):
        print(j, end="")
    
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()