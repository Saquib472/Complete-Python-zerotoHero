# Write a program to print the multiplicationn table of a number in reverse way.

num = int(input("Enter the number: "))
f = num * 10
print(f"{num}*{10}={f}")
for i in range(1,10):
    f = f - num
    print(f"{num}*{10-i}={f}")