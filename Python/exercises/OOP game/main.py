from player import Player

yoss = Player("yoss")

print(yoss.name)
print(yoss.get_name())
yoss._set_lives(5)


print(yoss)