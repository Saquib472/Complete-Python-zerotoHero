# Write a recursive function that can calculate sum of first n natural numbers.

def sumofna_rec(n):
    if n==1:
        return 1
    else:
        return n + sumofna_rec (n-1) 

res = sumofna_rec(4)
print(res)