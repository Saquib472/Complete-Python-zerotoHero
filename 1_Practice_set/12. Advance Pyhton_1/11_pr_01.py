# Write a python program to open three files 1.txt , 2.txt and 3.txt. if any of those files are not present , a message without exiting the program must be printed prompmting the same.

def readfile(filename):
    try:
        with open(filename) as f:
            a = f.read()
        print(a)

    except FileNotFoundError:
        print(f"file {filename} is not found!!")

readfile("1.txt")
readfile("4.txt")
readfile("2.txt")
readfile("3.txt")
