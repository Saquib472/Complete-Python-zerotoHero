def square (num):
    return num*num

l = [1, 3, 4, 6, 7]

# Method 1
# l2 = []
# for i in l:
#     l2.append(i*i)
# print(l2)

# Method 2
print(list(map(square,l)))