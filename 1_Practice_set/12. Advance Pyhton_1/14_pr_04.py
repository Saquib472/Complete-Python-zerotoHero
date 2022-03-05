# Write a program to display a/b where a and b are integers. if b = 0, display infinite by handling the ZeroDivisionError.

a = int(input("Enter the dividend: "))
b = int(input("Enter the divisor: "))

try:
     print(a/b)

except ZeroDivisionError:
    print("Infinite") 