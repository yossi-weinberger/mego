# List of first names
first_names = ["Rick", "Morty", "Summer", "Jerry", "Beth", "SpongeBob", "Patrick", "Squidward", "Mr. Krabs", "Sandy"]

# List of last names
last_names = ["Sanchez", "Smith", "Smith", "Smith", "Smith", "SquarePants", "Star", "Tentacles", "Krabs", "Cheeks"]

# List of phone numbers
phone_numbers = ["050-1234567", "051-2345678", "052-3456789", "053-4567890", "054-5678901", "055-6789012", "056-7890123", "057-8901234", "058-9012345", "059-0123456"]

alcoholic_beverages = ["Whiskey", "Vodka", "Rum", "Tequila", "Gin", "Beer", "Wine", "Champagne", "Sangria", "Martini"]

import random
from random import randint

# Randomly select a product
def rand_drink():
        return alcoholic_beverages[randint(0,9)]

def rand_price():
    return round(random.uniform(10, 100), 2)

# Generate a random quantity (between 1 and 10)
def rand_units():
    return randint(1, 10)

# Create the order document
def rand_order():
 return {
        "product": rand_drink(),
        "price": rand_price(),
        "units": rand_units(),
    }

#XML    
# for i in range(10):
#     print(f"<drink>\n"
#           f"    <ID>000{i}</ID>\n"
#           f"    <category>{categories[i]}</category>\n"
#           f"    <name>{names[i]}</name>\n"
#           f"    <brand>{brands[i]}</brand>\n"
#           f"    <price>{randint(15,90)}</price>\n"
#           f"</drink>")
    
#mongoDB
for i in range(10):
    print(f"{{\n"
          f"    'first name': '{first_names[i]}',\n"
          f"    'last name': '{last_names[i]}',\n"          
          f"    'phone': '{phone_numbers[i]}',\n"
          f"    'order': {rand_order()}\n"
          f"}},")    