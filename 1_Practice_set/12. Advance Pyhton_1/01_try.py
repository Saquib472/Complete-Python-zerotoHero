while(True):
    print("!!Press q to quit!!")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try: 
        print("Trying.......")
        a =int(a)  
        if a>6:
            print("You entered a number greater then 6")
    except Exception as e:
        print(f"Your input resulted an error: {e}")
        print("Please provide a valid number")

print("Thanks for playing this Game :-)")
