from random import randint
import lists
from turtle import Screen
from players import Players

# screen settings
screen = Screen()
screen.setup(width=600, height=400)

# vars
win_Coordinate = 240
Coordinate_y = 143
players = []
winner = 0
winner_color = ""

# creating turtles from class
for players_num in range(6):
    size = randint(1, 2)
    player = Players(lists.color[players_num], size, lists.color[players_num], -280, Coordinate_y)
    Coordinate_y -= 57
    players.append(player)

# pop-up bet window
user_bet = screen.textinput(title="Turtle race!", prompt="Type the color of the your bet: ")

# race
while player.turtle.xcor() < win_Coordinate:
    for player in players:
        player.race_moving()
        if player.turtle.xcor() >= win_Coordinate:
            break

# winner check
for player in players:
    if int(player.turtle.xcor()) >= winner:
        winner = player.turtle.xcor()
        winner_color = player.turtle.color()

print(user_bet)
print(winner_color[0])

# winner pop up msg
if winner_color[0] == user_bet:
    screen.textinput("winner", f"The winner is: {winner_color[0]} \nYOU WON!!!")
else:
    screen.textinput("loser", f"The winner is: {winner_color[0]} \nYOU LOST!")

screen.exitonclick()
