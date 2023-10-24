import random

print("Hi, i'm scripi the script and today we are going to play dice \ni will be the first:  \n")
player_a = random.randint(1, 6)
print(player_a)

if player_a <= 3:
    print("Oops, my chances are not the best :(")
else:
    print("Nice, good for me :)")

print("it's your turn now \ntype 'roll' to roll the dice")
player_b = input()
if player_b == "roll":
    player_b = random.randint(1, 6)
print(player_b)

if player_a > player_b:
    print("YES!!! I won!")
elif player_a < player_b:
    print("Nice!!! you won!")
elif player_a == player_b:
    print("It's a tie")
