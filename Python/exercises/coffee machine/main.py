import time
import graphics

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



# headline and graphics

# functions

def coin_trey(coin):
    if coin == "q":
        return 0.25
    if coin == "d":
        return 0.10
    if coin == "n":
        return 0.05
    if coin == "p":
        return 0.01
def make_coffee():
    coins = 0
    change = 0
    # showing coffee and prices
    for drink, price in menu.items():
        print(f"{drink}: {price['cost']}$")

    #Choosing coffee
    coffee_type = input("chose the type of coffee you want: ")
    for drink in menu:
        if coffee_type == drink:
            coffee_price = menu[coffee_type]["cost"]
            print (f"The price of your coffee is: {coffee_price}")

    #coin insert
    while coins < coffee_price:
        coin = input("insert your coins: ")
        coins += coin_trey(coin)
        print(f"You insert {coins}$")####
        change = coins - coffee_price

    #coffee making and change
    print("coffee in the making")
    for i in range(8):
        print ("-", end="" )
        time.sleep(0.5)
    print(f"\nYour coffee is rady\n{graphics.coffee}Take"
          f" {round(change,2)}$ change")

    def sum_profit():
        Profit = coffee_price
make_coffee()




sum_profit()
print(profit)


#run time
main_menu = input()
if main_menu == "":
    make_coffee()
elif main_menu == "off":
    reports()