# Write a python function to convert inches to cm

def conv(inch):
    return inch * 2.54

inches = int(input("enter the inche value: "))
cm = conv(inches)
print(f"{inches}inche == {cm}cm")