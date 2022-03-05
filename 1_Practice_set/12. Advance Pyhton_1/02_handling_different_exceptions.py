# try:
#     num = int(input("Enter a number: "))
#     print(f"{1/num}")
# except Exception as e:
#     print(e)

# print("Code is running continuous")

try:
    num = int(input("Enter a number: "))
    print(f"{1/num}")

except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero")

except ValueError as e:
    print("Please enter a valid number")

print("Code is running continuously")