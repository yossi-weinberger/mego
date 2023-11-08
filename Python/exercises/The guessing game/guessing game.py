import txt
import graphics

print (graphics.headline)

#random nuber between 0-100
from random import randint
random_num = randint(1, 100)

#select defculty
level = input("chose the difficulty (e/h): ")
print("Guess a number between 1-100")
if level == "h":
    difficulty = 5
elif level == "e":
    difficulty = 10

#showing treys left
def tryes_left(a, b):
    return a - b

#user input guess and chack
fail_try = 0
while fail_try < difficulty:
    print(f"you have {tryes_left(difficulty,fail_try)} tryes\n")
    guess = int(input("Type your guess: "))
    if guess > random_num:
        fail_try += 1
        print(f"{txt.too_big}\n")
    if guess < random_num:
        fail_try += 1
        print(f"{txt.too_small}\n")
    if guess == random_num:
        print (txt.win)
        break
else:
    print(f"{txt.game_over} {random_num}")
