# Write a program to print the following pattern.
# ***
# * *
# ***

n = int(input("Enter the number of rows you want to print: "))
print("*"*n)
for i in range(n-2):
    print("*", end="")
    print(" "*(n-2), end="")
    print("*")
print("*"*n)