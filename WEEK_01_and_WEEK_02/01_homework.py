#print table of n using user input in python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, 'x', i, '=', n*i)






#print a program to print a pattern of numbers in python
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()







# write a program to print the sum of first n natural numbers in python
n = int(input("Enter a number: "))
sum_natural = n * (n + 1) // 2
print("The sum of first", n, "natural numbers is:", sum_natural)
