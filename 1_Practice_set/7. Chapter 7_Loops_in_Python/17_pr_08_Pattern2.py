# Write a program to print the following pattern.
#   *
#  ***
# *****

line = int(input("Enter the number of rows you want to print: "))

for i in range(line):
    print(" "*(line-i-1), end="")
    print("*"*(2*i+1), end="")
    print(" "*(line-i-1))