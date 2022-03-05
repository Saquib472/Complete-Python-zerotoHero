a = [3,2,4,5,43,55,75,60,123,67,0,756]

# b = []
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)

b = [i for i in a if i%2==0]
print(b)

