print("Hi, Wellcom to the love finder")

lover1 = (input("Type your name please: "))
lover2 = (input("Type the name of your lover: "))
lovers = lover1.casefold() + lover2.casefold()
txt = "You have a match of "

sum = len(lovers)

num = lovers.count("t")
num += lovers.count("r")
num += lovers.count("u")
num += lovers.count("e")
num += lovers.count("l")
num += lovers.count("o")
num += lovers.count("v")

match = int((num / sum) * 100)

if match >= 60:
    print(f"{txt} {match}%\nYou are lucky!!! go make some baby's ")
elif match < 60 and match >= 20:
    print(f"{txt} {match}%\nYou can make it work, give it a try")
elif match < 20:
    print(f"{txt} {match}%\nThere are plenty of fish in the sea, it's not the one")

