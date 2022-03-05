# Write a list comprehension to print a list which contains the multiplication table of a user enetered number.

num = int(input("Enter your number: "))

l = [num*i for i in range(1,11)]
print(l)