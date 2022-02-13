# Create a class with a class attribute a ; create an object from it and set a directly using object a = 0. Does this change the class attribute ??

class Sample:
    a = "Saquib"


obj = Sample()
obj.a = "Rohan"

print(Sample.a)
print(obj.a)