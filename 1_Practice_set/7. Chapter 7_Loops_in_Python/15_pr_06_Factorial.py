# Write a program to find Factorial of a given number using for loop.
# Factorial of a number is the products of all the number from 1 to that number.
# Ex - 5! = 5*4*3*2*1

num = int(input("Enter the number: "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"The factorial of a given number is: {fact}")