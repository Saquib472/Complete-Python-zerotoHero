# Write a python function to remove a given word from a string and strip it at the same time

def remove_and_strip(string, word):
    nwstr = string.replace(word, "")
    return nwstr.strip()

strr = input("Enter the string: ")
wrd = input("Enter the word: ")
res = remove_and_strip(strr, wrd)
print(res)