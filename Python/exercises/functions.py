# function 1
def num_multiplication(x, y, z):
    print(x * y * z)


# function 2
def full_name():
    first_name = input("Type your first name: ")
    last_name = input("Type your family name: ")
    print(f"the full name is: {first_name} {last_name}")


# function 3
def biggest_num():
    num1 = int(input("Type the first number: "))
    num2 = int(input("Type the second number: "))
    num3 = int(input("Type the third number: "))
    numbers = [num1, num2, num3]
    print(f"The biggest number is: {max(numbers)}")


# function 4
def longest_name():
    name1 = input("Type the first name: ")
    name2 = input("Type the second name: ")
    name3 = input("Type the third name: ")
    names = [name1, name2, name3]

    len_name = 0
    for i in names:
        if len(i) > len_name:
            len_name = len(i)
            long_name = i
    print(f"The longest name is: {long_name} with {len_name} characters")


# function 5

def odd_or_even():
    x = int(input("type a number: "))
    if x % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


# function 6

def circle_area():
    from math import pi
    radius = float(input("type thr radius of your circle: "))
    area = pi * radius ** 2
    print(f"The area of your circle is: {area}")


# user call interface (for me for later use )
func = int(input("Type the number of function that you want to call (1-6):"))
if func == 1:
    num_multiplication(5, 5, 5)
if func == 2:
    full_name()
if func == 3:
    biggest_num()
if func == 4:
    longest_name()
if func == 5:
    odd_or_even()
if func == 6:
    circle_area()