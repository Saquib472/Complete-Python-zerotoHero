mydict = {
    "pankha":"fan",
    "dabba":"box",
    "bastu":"item"
}
print("Options are: ",mydict.keys())
a = input("Enter the hindi word: ")
# print("The meaning of the word is: ", mydict[a])
print("The meaning of the word is: ", mydict.get(a)) # --> It will not give an error