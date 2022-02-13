class Employee:
    company = "Google"
    def __init__(self, name, salary, subunit):
        print("Welcome to Employee Dashboard!!!!!")
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getEmpDetails(self):
        print(f"The Employee name is {self.name}")
        print(f"{self.name}'s salary is {self.salary}")
        print(f"{self.name}'s subunit is {self.subunit}")

saquib = Employee("Saquib",600000,"YuTube")
saquib.getEmpDetails()

# __init__ constructor runs as soon as the object is created.
