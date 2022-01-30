# Write a program to greet all the person names stored in a list l1 which starts with "S".

l1 = ["Rohan","Babita","Saquib","Alilm","Soyab"]

for name in l1:
    if name.startswith("S"):
        print(f"Hello {name}")