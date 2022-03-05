def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good!!!!") # raising custom error

a = increment('dhsvh')
print(a)