class Employee:
    company = "Google"
    def getSalary(self):
        print(f" saquib's salary for the {self.company} is {self.salary} ")

saquib = Employee()

saquib.salary = 30000
saquib.getSalary()
# Employee.getSalary(saquib) 

# saquib.getSalary() is internally working like Employee.getSalary(saquib) which takes 1 positional argument saquib object so if we don't give self argument then it'll show this error "getSalary() takes 0 positional arguments but 1 was given"


