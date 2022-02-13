class Employee:
    salary = 100 # Class Attribute

saquib = Employee()
ali = Employee()

saquib.salary = 300 # Instance Attribute

print(saquib.salary) # Giving preference to the instance attribute over class attribute
print(ali.salary) # This will print the salary from the class attribute