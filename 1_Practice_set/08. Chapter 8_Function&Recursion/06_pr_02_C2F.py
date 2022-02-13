# Celsius to Fahrenheit
def conv(c):
    return (c*1.8)+32

cent = int(input("enter the celcius: "))
result = conv(cent)
print(f"{cent}c == {result}f")