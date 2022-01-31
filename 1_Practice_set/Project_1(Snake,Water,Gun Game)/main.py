# Snake, Water, Game 

import random

def game(comp, you):
    if comp == "s":
        if you == "g":
            return True
        elif you == "w":
            return False
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
    elif comp == you:
        return None

print("Comp turns: Snake(s), Water(w), Gun(g)?")
randno = random.randint(1,3)
if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
elif randno == 3:
    comp = "g"

you = input("Your turns: Snake(s), Water(w), Gun(g)?")
res = game(comp, you)

print(f"Comp choosed {comp}")
print(f"You choosed {you}")

if res == None:
    print("This game is a tie!!")
elif res:
    print("Congrats!! You win the game :-)")
else:
    print("You loose :-(")
