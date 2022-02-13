# Write a program to find sum of first n Natural numbers.
# Natural number starts from 1 and upto infinity.

num = int(input("Enter the number: "))
total = 0
# for i in range(1,num+1):
#     total = total + i
# print(f"The sum of first {num} natural number is: {total}")

# Using while loop.
i = 1
while i<=num:
    total = total+i
    i = i+1
print(f"The sum of first {num} natural number is: {total}")