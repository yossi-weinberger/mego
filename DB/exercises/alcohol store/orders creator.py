import random

# List of alcoholic beverages
alcoholic_beverages = ["Whiskey", "Vodka", "Rum", "Tequila", "Gin", "Beer", "Wine", "Champagne", "Sangria", "Martini"]

# Empty list to store order documents
orders = []

# Generate 10 order documents
for _ in range(10):
    # Randomly select a product
    product = random.choice(alcoholic_beverages)
    
    # Generate a random price (between 10 and 100)
    price = round(random.uniform(10, 100), 2)
    
    # Generate a random quantity (between 1 and 10)
    units = random.randint(1, 10)
    
    # Create the order document
    order = {
        "product": product,
        "price": price,
        "units": units
    }
    
    # Add the order document to the list
    orders.append(order)
    print(orders)
