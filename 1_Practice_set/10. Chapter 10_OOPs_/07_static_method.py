class Employee:
    company = "Youtube"
    def getSalary(self, sign):
        print(f"Saquib's salary for the {self.company} is {self.salary}\n{sign}")

    @staticmethod
    def greet():
        print("Good Morning despacito!!!")

saquib = Employee()

saquib.salary = 300000

saquib.getSalary("Thanks!")

saquib.greet()