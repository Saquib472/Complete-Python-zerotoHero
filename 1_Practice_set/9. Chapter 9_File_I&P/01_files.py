# Using Open function to load and read function to read the content of a file 
# by default the mode is "r"

f = open("sample.txt","r")
data = f.read()
# data = f.read(5) # read the first 5 contents of a file.
print(data)
f.close()


