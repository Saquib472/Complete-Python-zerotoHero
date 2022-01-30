# Write a program to print the multiplication table of given number using while loop.

num = int(input("enter the number: "))
i = 1
while i <11:
    print(f"{num}*{i}={num*i}")
    i = i+1