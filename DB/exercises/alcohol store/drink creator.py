# List of alcoholic beverages
alcoholic_beverages = ["Whiskey", "Vodka", "Rum", "Tequila", "Gin", "Beer", "Wine", "Champagne", "Sangria", "Martini"]

# List of brands
brands = ["Jack Daniels", "Absolut", "Bacardi", "Patron", "Beefeater Gin", "Heineken", "Merlot", "Moet", "Real Sangria", "Martini Rosso"]

# List of categories of alcoholic beverages
categories = ["Spirits", "Liqueurs", "Wines", "Beers", "Ciders", "Meads", "Sakes", "Sojus", "Vermouths", "Aperitifs"]


# List of invented names for alcoholic beverages
names = ["Ginger Whiskey", "Forest Fruit Vodka", "Caramel Rum", "Spicy Tequila", "Citrus Gin", "Dark Beer", "Sweet Wine", "Fruity Champagne", "Tropical Sangria", "Bitter Martini"]


from random import randint

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
          f"    'ID': '000{i}',\n"
          f"    'category': '{categories[i]}',\n"
          f"    'name': '{names[i]}',\n"
          f"    'brand': '{brands[i]}',\n"
          f"    'price': {randint(15,90)}\n"
          f"}},")    