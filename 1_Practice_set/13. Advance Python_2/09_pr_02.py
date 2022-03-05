# write a program to input name , marks and phone number of a student. format it using the format function.

name = input("enter your name: ")
marks = int(input("enter your marks: "))
ph = input("enter your phone number: ")

sent = "The name of the student is {},\n his marks are {} and\n his phone number is {}".format(name,marks,ph)

print(sent)