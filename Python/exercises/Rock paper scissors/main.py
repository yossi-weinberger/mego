import pics
import random
pics = [pics.rock,pics.paper,pics.scissors]

#txt vars
tie = ("it's a tie")
win = ("You won")
lose = ("You lose")

#player 1 move
print("Hi, lets play")
player_1 = (input("type rock paper or scissors\n"))

#player 1 pic show
if player_1 == "rock":
    print(pics[0])
if player_1 == "paper":
    print(pics[1])
if player_1 == "scissors":
    print(pics[2])

#player 2 random
moves = ["rock","paper","scissors"]
random_play = random.randint(0,2)
player_2 = (moves[random_play])

#player 2 move and pic show
print(f"I choose\n{player_2}\n{pics[random_play]}")

#rools and winner
if player_1 == player_2:
    print(tie)
elif player_1 == "paper" and player_2 == "rock":
    print(win)
elif player_1 == "scissors" and player_2 == "paper":
    print(win)
elif player_1 == "rock" and player_2 == "scissors":
    print(win)
else:
    print(lose)

