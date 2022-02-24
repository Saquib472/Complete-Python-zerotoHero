# Create a class pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.

class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "Black"

class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow !!!!") 

d = Dog()
print(d.animalType , d.color)
d.bark()