# Write a program to read the text from agiven file poem.txt and find out whether it contains the word twinkle.

f = open("poems.txt")
p = f.read()

if "twinkle" in p:
    print("Twinkle is present")
else:
    print("Twinkle is not present")

f.close()