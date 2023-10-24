print("Hi, Wellcom to Pizza pazzzz")
size = (input("Type the size of the Pizza please (L/M/S): ")).casefold()

l_price = 25
m_price = 20
s_price = 15
pineapple = 0
mushrooms = 0
olives = 0
Cheese = 3
txt = "The total price of your pizza is: "

if size == "l":
    total_price = l_price
    pineapple = 6
    mushrooms = 5
    olives = 5
elif size == "m":
    total_price = m_price
    pineapple = 4
    mushrooms = 5
    olives = 5
elif size == "s":
    total_price = s_price
    pineapple = 2
    mushrooms = 2
    olives = 2

pine = (input("Do you want to add pineapple on your Pizza? ")).casefold()
if pine == "yes":
    total_price += pineapple
mush = (input("Do you want to add mushrooms on your Pizza? ")).casefold()
if mush == "yes":
    total_price += mushrooms
olive = (input("Do you want to add olives on your Pizza? ")).casefold()
if olive == "yes":
    total_price += olives
add_Cheese = (input("Do you want to add Cheese on your Pizza? ")).casefold()
if add_Cheese == "yes":
    total_price += Cheese
    print("Vary good!!!, Cheese is very tasty")

print(f"{txt}{total_price}$")
