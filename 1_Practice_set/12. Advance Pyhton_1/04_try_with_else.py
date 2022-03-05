try:
    num = int(input("Enter a number: "))
    a = 1/num
    print(a)

except Exception as e:
    print(e)

else:
    print("Program runs successfull") # else block will execute only if the try block will run successfully.