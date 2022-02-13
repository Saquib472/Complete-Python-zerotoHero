# Write a program to print following pattern:
# *
# **
# ***
# ****

line = int(input("Enter the number of rows you want to print: "))

for i in range(1,line+1):
    print("*" * i)