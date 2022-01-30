mydict = {
    "Fast": "In a quick manner",
    "Harry" : "A coder",
    "Marks": [1,2,3],
    "anotherdic": {"harry":"player"}
}

print(mydict["Fast"])
print(mydict["Harry"])
print(mydict["Marks"])
print(mydict["anotherdic"])
print(mydict["anotherdic"]["harry"])

# Mutable
mydict["Marks"] = [20,30,4]
print(mydict["Marks"])