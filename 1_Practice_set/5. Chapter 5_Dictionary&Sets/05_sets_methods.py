# Create an empty set
a = set()
print(type(a))

# Adding values to an empty set
a.add(4)
a.add(3)
a.add(5)
a.add(5) # --> Adding a value repeatedly can not change the set
a.add(4)
a.add((3,2,1)) # --> Can not add list or dictionary in a set but you can add tuple
print(a)

print(len(a)) # --> Length of set

a.remove(5)
print(a)

a.pop() # --> Remove a random value from the set
print(a)