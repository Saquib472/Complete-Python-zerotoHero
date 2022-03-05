# Write a program to filter a list of numbers which are divisible by 5.

div_5 = lambda a : a%5==0

l = [1,2,3,4,5,6,7,8,9,0,76,87,98]

res = list(filter(div_5,l))

print(res)