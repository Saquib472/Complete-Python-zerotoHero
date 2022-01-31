from unittest import result


# def factorial(n):
#     _factorial = 1
#     for i in range(n):
#         _factorial = _factorial*(i+1)
#     return _factorial

# num = int(input("enter the number: "))
# result = factorial(num)
# print(f"Factorial of the given number is {result}")

def factorial_rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_rec(n-1)

num = int(input("enter the number: "))
result = factorial_rec(num)
print(f"Factorial of the given number is {result}")