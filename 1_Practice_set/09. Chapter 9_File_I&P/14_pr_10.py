# Write a python program to wipe out the contents of a file.

filename = "this.txt"

with open(filename, "w") as f:
    f.write("")