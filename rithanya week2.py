# Define base drinks based on first letter of name
def get_base_drink(name):
    first_letter = name[0].lower()
    if first_letter in 'abc':
        return "Espresso"
    elif first_letter in 'def':
        return "Latte"
    elif first_letter in 'ghi':
        return "Cappuccino"
    elif first_letter in 'jkl':
        return "Americano"
    elif first_letter in 'mno':
        return "Mocha"
    elif first_letter in 'pqr':
        return "Macchiato"
    else:
        return "Flat White"

# Pick ingredients based on base drink
def choose_ingredients(base):
    if base == "Espresso":
        return "Hazelnut", "Oat Milk", "Honey", "Cocoa Powder"
    elif base == "Latte":
        return "Vanilla", "Almond Milk", "Sugar", "Whipped Cream"
    elif base == "Cappuccino":
        return "Pumpkin Spice", "Whole Milk", "Maple Syrup", "Cinnamon"
    elif base == "Americano":
        return "Caramel", "Coconut Milk", "Stevia", "Chocolate Syrup"
    elif base == "Mocha":
        return "Chocolate", "Soy Milk", "Agave Syrup", "Marshmallows"
    elif base == "Macchiato":
        return "Cinnamon", "Oat Milk", "Honey", "Cocoa Powder"
    else:  # Flat White
        return "Vanilla", "Whole Milk", "Sugar", "Cinnamon"

# Main recipe generator
def generate_recipe(name):
    base = get_base_drink(name)
    flavor, milk, sweetener, topping = choose_ingredients(base)

    print(f"\nHi {name.title()}! Here's your personalized café recipe:\n")
    print(f"Base Drink: {base}")
    print(f"Flavor Shot: {flavor}")
    print(f"Milk Type: {milk}")
    print(f"Sweetener: {sweetener}")
    print(f"Topping: {topping}")
    print("\nInstructions:")
    print(f"1. Brew a shot of {base}.")
    print(f"2. Add a pump of {flavor} syrup.")
    print(f"3. Steam and froth {milk}, then pour over the base.")
    print(f"4. Sweeten with {sweetener} to taste.")
    print(f"5. Top with {topping}.")
    print("6. Serve and enjoy!")

# Run it
if __name__ == "__main__":
    user_name = input("Enter your name to get your custom café recipe: ")
    generate_recipe(user_name)
