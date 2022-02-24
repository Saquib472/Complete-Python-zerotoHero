# Write a program that generates a random number and askes the user to guess it.
# If the player's guess is higher than the actual number, the program displays "Lower number please".
# similarly id the user's guess is too low, the program prints "higher number please".
# when the user guess the corrects number, the program displays the number of guesses the player used to arrive the number.
# Hint: use the random module.

import random
randNumber = random.randint(1,100)
# print(randNumber)

userGuess = None
guesses = 0

while(userGuess !=randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses+=1
    if userGuess == randNumber:
        print("You guessed it write!!!")
    else:
        print("You guessed it wrong!!!")
        if userGuess>randNumber:
            print("!!!Enter a smaller number!!!")
        elif userGuess<randNumber:
            print("!!!Enter a larger number!!!")


print(f"You guessed the number in {guesses} guesses")

with open("highscore.txt","r") as f:
    high = int(f.read())

if high>guesses:
    print("Congo!! You just broke the highscore :-)")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))