try:
    num = int(input("Enter a number: "))
    a = 1/num
    print(a)

except Exception as e:
    print(e)
    exit()

finally:
    print("We are done!!!!") # finally will run regardelessly even the except will exit the program.

print("Thanks for using the program!!!")