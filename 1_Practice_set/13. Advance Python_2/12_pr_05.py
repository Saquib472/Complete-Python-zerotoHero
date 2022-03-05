# Write a program to find the maximum of the numbers in a list using reduce function.

from functools import reduce

l = [1,2,3,4,5,6,7,8,9,0,76,87,98]

val = reduce(max, l)

print(val)
