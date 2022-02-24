# Single Inheritance

class Employee:
    company = "Google"
    language = "C"
    def showDetails(self):
        print("This is an Employee")

    def getLang(self):
        print(f"The language is {self.language}")

class Programmer(Employee):
    language = "Python"
    def getLang(self):
        print(f"The language is {self.language}")

e = Employee()
p = Programmer()

e.showDetails()
print("********Inheriting the methods and attributes from the Employee Class********")
p.showDetails()
print(p.company)

print("*****************Over writing the methods********************")
e.getLang()
p.getLang()