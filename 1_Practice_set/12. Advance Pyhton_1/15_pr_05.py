num = int(input("Enter your number: "))

l = [num*i for i in range(1,11)]
print(l)

with open("tables.txt", "a") as f:
    f.write(str(l))
    f.write("\n")