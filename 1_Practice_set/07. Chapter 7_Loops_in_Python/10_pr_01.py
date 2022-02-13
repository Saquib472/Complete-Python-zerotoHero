# Write a program to print multiplication table of a given number.

num = int(input("Enter the number, you wants the multiplication for:  "))
for i in range(1,11):
    # print(str(num) +" * "+ str(i) +" : ", num*i)
    print(f"{num}*{i}={num*i}") # --> f string 