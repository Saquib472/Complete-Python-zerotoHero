# Write a function that can print the following pattern
# *****
# ****
# *** 
# **  
# * 

def pattern(n):
    for i  in range(n):
        print("*" * n)
        n-=1

pattern(5)