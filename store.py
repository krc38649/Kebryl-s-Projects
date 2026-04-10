"""A dictionary with shoe brands and multiple models from each brand, each with a mileage limit and a price."""
shoes = {
    "Nike": {
        "Air Zoom Pegasus": {"price": 120, "quality": "Budget", "mileage_limit": 300},
        "Air Zoom Vomero": {"price": 150, "quality": "Mid Range", "mileage_limit": 400},
        "Air Zoom Alphafly": {"price": 250, "quality": "High End", "mileage_limit": 500}
    },
    "Adidas": {
        "Adizero Adios": {"price": 160, "quality": "Budget", "mileage_limit": 300},
        "Adizero Boston": {"price": 180, "quality": "Mid Range", "mileage_limit": 400},
        "Ultra Boost": {"price": 230, "quality": "High End", "mileage_limit": 500}
    },
    "Brooks": {
        "Ghost": {"price": 130, "quality": "Budget", "mileage_limit": 300},
        "Glycerin": {"price": 150, "quality": "Mid Range", "mileage_limit": 400},
        "Levitate": {"price": 160, "quality": "High End", "mileage_limit": 500}
    },
    "Asics": {
        "Gel Cumulus": {"price": 110, "quality": "Budget", "mileage_limit": 300},
        "Gel Nimbus": {"price": 140, "quality": "Mid Range", "mileage_limit": 400},
        "Gel Kayano": {"price": 160, "quality": "High End", "mileage_limit": 500}
    }
}

"""The store menu, where players can buy new shoes, it shows a list of brands that users can choose from, once they choose a brand it will display a list of available models from that brand, once they choose a model it will check if they have enough money to buy the shoes, if they do it will update their shoe mileage limit and deduct the price from their money. As well as assign the new shoe to the player dictionary (USER SELECTS MODELS AND BRANDS USING NUMBERS"""
def store_menu():
    from player import player
    from functions import clear_screen
    clear_screen()
    print("\n===== SHOE STORE =====")
    print("You walk into the shoe store and a funny looking salesman greets you. He says 'Welcome to the best shoe store in town! We have the best shoes for all your running needs!'")
    print("Your current shoe mileage is: ", player["shoe_mileage"])
    print("Your current money is: ", player["money"])
    print("\nAvailable Brands:")
    brands = list(shoes.keys())
    for i, brand in enumerate(brands, 1):
        print(f"{i}. {brand}")
    try:
        brand_choice = int(input("Select a brand by number, to go back to the menu press 0: ")) - 1
    except ValueError:
        print("Please enter a number.")
        return
    if brand_choice < 0 or brand_choice >= len(brands):
        print("Invalid choice. Returning to main menu.")
        return
    selected_brand = brands[brand_choice]
    print(f"\nAvailable Models from {selected_brand}:")
    models = list(shoes[selected_brand].keys())
    for i, model in enumerate(models, 1):
        price = shoes[selected_brand][model]["price"]
        mileage_limit = shoes[selected_brand][model]["mileage_limit"]
        print(f"{i}. {model} - Price: ${price}, Mileage Limit: {mileage_limit} miles")
    try:
        model_choice = int(input("Select a model by number, press 0 to go back to the menu: ")) - 1
    except ValueError:
        print("Please enter a number.")
        return
    if model_choice < 0 or model_choice >= len(models):
        print("Invalid choice. Returning to main menu.")
        return
    selected_model = models[model_choice]
    price = shoes[selected_brand][selected_model]["price"]
    mileage_limit = shoes[selected_brand][selected_model]["mileage_limit"]
    if player["money"] < price:
        print("You don't have enough money to buy this shoe. Returning to main menu.")
        return
    player["money"] -= price
    player["shoe_mileage"] = 0
    player["shoes"] = f"{selected_brand} {selected_model}"
    print(f"You have successfully purchased the {selected_brand} {selected_model}!")
    print(f"Your new shoe mileage limit is: {mileage_limit} miles")
    print(f"Your remaining money is: ${player['money']}")
    input("Press Enter to return to the main menu...")
    player["shoe_quality"] = shoes[selected_brand][selected_model]["quality"]