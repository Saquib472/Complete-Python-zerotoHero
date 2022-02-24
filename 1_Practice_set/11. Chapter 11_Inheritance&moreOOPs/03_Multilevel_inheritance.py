class Person:
    country = "India"

    def takeBreath(self):
        print("I'm breathing....")

class Employee(Person):
    company = "Honda"
    salary = 300000 
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I'm an Employee so I'm thora thora breathing mah boiiii...")

class Programmer(Employee):
    company = "Fiver"

    def getSalary(self):
        print("No salary sad life....")

pe = Person()
em = Employee()
pr = Programmer()

pe.takeBreath()
em.takeBreath()
pr.takeBreath()
print("*********************************************")

em.getSalary()
pr.getSalary()
print("*********************************************")

print(em.company)
print(pr.company)
