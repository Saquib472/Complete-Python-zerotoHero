# Can you change the self parameter inside a class to something else (say for example saquib). Try to change self to "slf" or "saquib" or anything you want and see the effect.

# class Sample:
#     def __init__(self, name):
#         self.name = name

# obj = Sample("saquib")
# print(obj.name)

class Sample:
    def __init__(slf, name):
        slf.name = name

obj = Sample("saquib")
print(obj.name)

# The answer is yes you can but it is better to use self cz it is easily readable and understandale by the others.