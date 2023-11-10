import time
import graphics

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 1.80,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 2.0,
    }
}

ingredients = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = {
    "change": 50,
    "profit": 0,
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0,
}


# functions
def coin_trey(coin):
    if coin == "q":
        money["quarters"] += 1
        return 0.25
    if coin == "d":
        money["dimes"] += 1
        return 0.10
    if coin == "n":
        money["nickels"] += 1
        return 0.05
    if coin == "p":
        money["pennies"] += 1
        return 0.01


def make_coffee():
    coins = 0
    change = 0
    # showing coffee and prices
    print("\nmenu - coffee prices")
    for drink, price in menu.items():
        print(f"{drink}: {price['cost']}$")

    # Choosing coffee and checking ingredients
    coffee_type = input("\nchose the type of coffee you want: ")
    if coffee_type == "off":
        technician_mode()
    if (ingredients["water"] < menu[coffee_type]["ingredients"]["water"]
            or ingredients["coffee"] < menu[coffee_type]["ingredients"]["coffee"]
            or ingredients["milk"] < menu[coffee_type]["ingredients"]["milk"]):
        print("There is NOT enough ingredients to make you this coffee")
        run_time()

    for drink in menu:
        if coffee_type == drink:
            coffee_price = menu[coffee_type]["cost"]
            print(f"\nThe price of your coffee is: {coffee_price}$")

    # coin insert
    while coins < coffee_price:
        coin = input("insert your coins (q/p/n/d): ")
        coins += coin_trey(coin)
        print(f"\nYou insert {round(coins, 2)}$")
        change = coins - coffee_price

    # coffee making and change
    print("Your coffee is in the making")
    for i in range(6):
        print(" > ", end="")
        time.sleep(0.5)
    print(f"\nYour coffee is rady\n{graphics.coffee}Take"
          f" {round(change, 2)}$ change")

    # insert profit and ingredients value
    money["profit"] += coffee_price
    ingredients["water"] -= menu[coffee_type]["ingredients"]["water"]
    ingredients["coffee"] -= menu[coffee_type]["ingredients"]["coffee"]
    ingredients["milk"] -= menu[coffee_type]["ingredients"]["milk"]


def technician_mode():
    password = input("Type the password: ")
    if password == "1234":
        select_report = int(input("\nfor ingredients report type 1: \n"
                                  "for money report type 2: \n"
                                  "to insert more ingredients type 3: \n"
                                  "to exit press 4: "))
        if select_report == 1:
            for ingredient_report, amount in ingredients.items():
                print(f"{ingredient_report} : {amount}")
            technician_mode()
        elif select_report == 2:
            for money_report, amount in money.items():
                print(f"{money_report} : {amount}")
            technician_mode()
        elif select_report == 3:
            ingredients["water"] += int(input("Type the amount of water to add: "))
            ingredients["coffee"] += int(input("Type the amount of coffee to add: "))
            ingredients["milk"] += int(input("Type the amount of milk to add: "))
            technician_mode()
        elif select_report == 4:
            run_time()
    else:
        print("Wrong password!!!\n")
        run_time()


# actual run time
print(graphics.vending_machin)


def run_time():
    user_interface = "on"
    while user_interface != "off":
        make_coffee()
        user_interface = input("To buy coffee press ENTER: ")
        if user_interface == "off":
            technician_mode()
            user_interface = input("To go back to user interface type 'on': ")


run_time()
