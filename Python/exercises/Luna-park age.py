pic_price = 5
roller_price = 20
slide_price = 10
ballpool_price = 5
pay_txt = "You need to pay"

age = int(input("Please insert your age: "))

if age >= 18:
    height = int(input("Please insert your height: "))
    if height >= 120:
        print("You can go to the roller coaster")
        pic = input("Do you want your picture taken?: ").casefold()
        if pic[0] == "y":
            print(f"{pay_txt} {pic_price}$ for the picture and"
                  f" {roller_price}$ for the roller coaster")
        if pic[0] == "n":
            print(f"{pay_txt} {roller_price}$")
    else:
        print("You can go to the slide")
        print(f"{pay_txt} {slide_price}$")
else:
    print("You can go to the ball pool")
    print(f"{pay_txt} {ballpool_price}$")
