# Write a program to find whether your name is present in the list or not.

names = ["saquib","mousumi","bandana","soyeb","khali","sahanaj","alim"]
name = input("Enter your name to check: ")
name = name.lower()

if name in names:
    print("Your name present in the list!!")
else:
    print("Your name is not present in the list!!!")