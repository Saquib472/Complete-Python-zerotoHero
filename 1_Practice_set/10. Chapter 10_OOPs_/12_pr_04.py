# Add a static method in problem 2 to greet the user with hello.

from cmath import sqrt
class Calculator:
    def __init__(self, num):
        self.num = num

    def squareNum(self):
        print(f"Square of {self.num} is {self.num**2}")

    def cubeNum(self):
        print(f"Cube of {self.num} is {self.num**3}")

    def squareRoot(self):
        print(f"Square root of {self.num} is {sqrt(self.num)}")

    @staticmethod
    def greet():
        print("Hello my friend !!!")


num = int(input("Enter the number: "))
en = input("what do you want to do Square, Cube, Squareroot or all ? type it properly: ")

obj = Calculator(num)

if en == "Square":
    obj.squareNum()
elif en == "Cube":
    obj.cubeNum()
elif en == "Squareroot":
    obj.squareRoot()
else:
    obj.squareNum()
    obj.cubeNum()
    obj.squareRoot()

obj.greet()