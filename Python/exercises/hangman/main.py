import graphics
import text
import random

# choosing Rendon word
random_num = random.randint(0, 12)
city = (text.citys[random_num])

# createing 2 list  for city and empty latters
empty = list("_" * len(city))
empty_letters = (' '.join(empty))
city_letters = list(city)

# vars
game_play = True
fail_tries = 0
success = 0


def win():
    print(graphics.win)
    global game_play
    game_play = False


def game_over():
    print(f"{graphics.game_over} \n The word was: {city}")
    global game_play
    game_play = False


def fail_msg():
    global fail_tries
    print(graphics.hangman[fail_tries])
    fail_tries += 1
    print(f"You are wrong, you lost {fail_tries}/7 tries ")
    print(' '.join(empty))


def play():
    fail = 0
    guess = input("Type one letter: ")
    for i in range(0, len(city)):
        if guess == city_letters[i]:
            print("\nNice! You guessed one letter successfully")
            empty[i] = guess
            city_letters[i] = "_"
            print(' '.join(empty))
            global success
            success += 1
            fail = 1
            break
    if fail == 0:
        fail_msg()
    if success == len(city):
        win()
    if fail_tries == 7:
        game_over()


# game play
print(graphics.game_name)
print(empty_letters)

while game_play == True:
    play()