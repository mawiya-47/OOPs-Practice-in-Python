# Print table of n in python using input like c++
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")





#write a program to print the sum of first n natural numbers in python using input like c++ 
n = int(input("Enter a number: "))
sum_natural = n * (n + 1) // 2
print(f"The sum of first {n} natural numbers is: {sum_natural}")






#write a program to print the sum of first n even numbers in python using input like c++
n = int(input("Enter a number: "))
sum_even = n * (n + 1)
print(f"The sum of first {n} even numbers is: {sum_even}")