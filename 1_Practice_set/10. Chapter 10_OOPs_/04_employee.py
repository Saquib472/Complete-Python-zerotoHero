# Class Attribute

class Employee:
    company = "Google"

saquib = Employee()
najmush = Employee()

print(saquib.company)
print(najmush.company)

Employee.company = "Youtube" # Changing the value of the class attribute

print(saquib.company)
print(najmush.company)