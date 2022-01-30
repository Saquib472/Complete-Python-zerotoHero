mydict = {
    "fast": "In a quick manner",
    "harry" : "A coder",
    "marks": [1,2,3],
    "anotherdic": {"harry":"player"},
    1: 2
}

# Dictionary methods
print(mydict.keys()) # --> Prints the keys of the dictionary
print(type(mydict.keys()))
print(list(mydict.keys()))

print(mydict.values()) # --> Prints the values of the dictionary

print(mydict.items()) # --> Prints the (key, value) for all contents of the dictionary

print(mydict)
updatedict = {
    "Lavish":"My Friend",
    "Diviya": "Best Friend",
    "Guru": "Goruuuuu"
}
mydict.update(updatedict) # --> Update the dictionary by adding updatedict to the dictionary
print(mydict)

print(mydict.get("harry")) # --> Print te value associated with "harry"
print(mydict["harry"]) # --> Print te value associated with "harry"

print(mydict.get("harry2")) # --> It returns None as the key is not avaiable in the dictionary
print(mydict["harry2"]) # --> It throws ERROR as the key is not available in the dictionary