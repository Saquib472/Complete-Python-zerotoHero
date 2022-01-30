greeting = "Hello, "
name = "Saquib"
c = greeting+name # --> Concatination of strings
# print(c)

# Indexing of a string
# print(name[0])
# print(name[4])
# name[3] = 'd' --> Does not work, you can't change a character in a string

# Slicing
print(name[:])
print(name[0:3])
print(name[:3])
print(name[0:])
print(name[1:4])
print(name[-4:-1]) # --> negative slicing
print(name[0::2])  # --> Slicing with skip value