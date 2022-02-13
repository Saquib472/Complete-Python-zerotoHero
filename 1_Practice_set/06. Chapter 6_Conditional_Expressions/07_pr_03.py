# A spam comment is defined as a text containing following keywords: "make a lot of money","buy now","subscribe this","click this". Write a program to detect this spams.

text = input("Enter your comment: ")

if "make a lot of money" in text:
    spam = True
elif "buy now" in text:
    spam = True
elif "subscribe this" in text:
    spam = True
elif "click this" in text:
    spam = True
else:
    spam = False

if spam == True:
    print("This text is spam!!!")
else:
    print("This text is not spam!!!")