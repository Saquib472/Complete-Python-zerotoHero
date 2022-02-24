class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6000

    # getter method
    @property # property decoretor is use to create a function as a property.
    def totalSalary(self):
        return self.salary + self.salarybonus

    # setter method
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)

print("**************************************")

e.totalSalary = 5800
print(e.totalSalary)
print(e.salary)
print(e.salarybonus)