# Assume a Game function in a program lets a user play a Game and returns the score as an integer. you need to read a file highscore.txt which is either blank or contains the previous highest score. you need to write a program to update the high score whenever game() breaks the highest score.

def game(h):
    return h

h = int(input("enter your highest score: "))
score = game(h)

with open("highscore.txt") as f:
    highscorestr = f.read()

if highscorestr == '':
    with open("highscore.txt", "w") as f:
        f.write(str(score))
elif int(highscorestr)<score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))