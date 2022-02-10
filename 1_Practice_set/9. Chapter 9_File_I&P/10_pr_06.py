# Write a program to mine a log file and find out wether it contains 'python'

with open("log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes python is present")
else:
    print("NO python is not present")