f = open("sample.txt","r")
# Read the first line
data = f.readline()
print(data)

# Read the second line and sooo onn...
data = f.readline()
print(data)
f.close()