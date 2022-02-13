# Write a python function to print multiplication table of a given number

def mult(n):
    for i in range(1,11):
        print(f"{n}*{i}=={n*i}")

number = int(input("Enter the number: "))
mult(number)
