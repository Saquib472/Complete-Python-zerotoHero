# Write a program to find whether a given username contains less then 10 characters or not.

user_name = input("Enter a user name: ")

if len(user_name)<10:
    print("Invalid user name. It should contains atleast 10 characters!!!")
else:
    print("Varified!")