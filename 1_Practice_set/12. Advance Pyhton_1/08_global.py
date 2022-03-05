# a = 54 # Global Variable
# def func1():
#     a = 8 # Local Variable
#     print(a)
# func1()
# print(a)

###############################################################

a = 54 # Global Variable
def func1():
    global a
    print(a)
    a = 8 # Local Variable
    print(a)
func1()
print(a)