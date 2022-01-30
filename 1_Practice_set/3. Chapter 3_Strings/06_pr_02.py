letter = '''Dear <|Name|>,
Greetings from Innomatics.
You are selected!
Date: <|Date|>
'''
name = input("Enter your name:\n")
date = input("Enter the Date:\n")

letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)

print(letter)