# Write a program to find whether a given number is Prime or not.
# A number is called Prime number when it has only two factors 1 and the number itself means you can only divide the number by 1 and the number itself, from 2 to n no number can divide the number except 1 and the number itself.

num = int(input("Enter the number: "))
prime = True
for i in range(2,num):
    if num%i == 0:
        prime = False
        break
if prime:
    print("The number is prime.")
else:
    print("The number is not prime")