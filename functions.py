import os
from player import player
import random
#GENERAL FUNCTIONS------------------------------------------------------------------------------------------------
"""Clearing the Console"""
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

"""returning to menu"""
def return_to_menu():
    response = input("\nPress Enter to return to the main menu...").split()
    if len(response) >0 and response[0].upper() == "QUIT":
        print("Exiting game. Goodbye!")
        exit()
    return

"""Deciding how many miles the runner can do per week based on their fitness"""
def safe_mileage():
    from player import player
    fitness = player["fitness"]
    if fitness < 20:
        return 15
    elif fitness < 40:
        return 30
    elif fitness < 60:
        return 40
    elif fitness < 80:
        return 50
    else:
        return 60



#FUNCTIONS FOR END OF WEEK UPDATES----------------------------------------------------------------------------------
def update_fitness(miles_run):
    from player import player
    target_mileage = safe_mileage()

    if miles_run <= target_mileage*0.5:
        player["fitness"] -= 1
        player["health"] += 4
    elif miles_run <= target_mileage:
        player["fitness"] += 1
    elif miles_run >= target_mileage*1.2:
        player["fitness"] += 2
        player["health"] -= 5
    else: #overtraining
        player["fitness"] += 1
        player["health"] -= 15
    player["shoe_mileage"] += miles_run
    clamp_stats()


"""Health Related functions"""
def health_update():
    clear_screen()
    print ("Health Update:")
    if player["health"] <= 25:
        print("Your health is at 25% or lower, you should definitely it easy this week.")
    elif player["health"] <= 50:
        print("Your health is at 50% or lower, you should really consider taking it easy this week.")
    elif player["health"] <= 75:
        print("Your health is at 75% or lower, you might want to take it a little easy this week.")
    else:
        print("Your health is in good shape, you can train as normal this week.")

    if player["weekly_intensity"] == "Hard":
        player["health"] -= 2
    if player["weekly_intensity"] == "Easy":
        player["health"] += 2

    input("Press Enter To Continue")


"""Telling the player how much fitness they have gained or lost after they advance to the next week, and giving them a recommendation for how much to run next week"""
def fitness_update(miles_run):
    clear_screen()
    target_mileage = safe_mileage()
    print("Fitness Update:")
    if miles_run <= target_mileage*0.5:
        fitness_change = -1
    elif miles_run <= target_mileage:
        fitness_change = 1
    elif miles_run >= target_mileage*1.2:
        fitness_change = 2
    else: #overtraining
        fitness_change = 1

    clamp_stats()

    if fitness_change > 0:
        print(f"You gained {fitness_change} fitness points this week!")
    elif fitness_change < 0:
        print(f"You lost {-fitness_change} fitness points this week.")
    else:
        print("Your fitness level remained the same this week.")

    print(f"Based on your current fitness level, we recommend running around {target_mileage} miles next week to maximize your fitness gains without risking injury.")

    input("Press Enter To Continue")

def experience_gained():
    clear_screen()

    gained=0
    intensity = player["weekly_intensity"]

    if intensity == "Easy":
        gained = 1
    if intensity == "Normal":
        gained = 2
    if intensity == "Hard":
        gained =3


    print("Experience Update:")
    print(f"You gained {gained} experience points this week!")
    clamp_stats()

    player["experience_points"] += gained
    input("Press Enter To Continue")



""""Keeping the stats in the correct range"""
def clamp_stats():
    player["health"] = max(0, min(player["health"], 100))
    player["fitness"] = max(0, min(player["fitness"], 100))
    player["shoe_mileage"] = max(0, player["shoe_mileage"])



"""Shoe checker"""
def shoe_check():
    mileage= player["shoe_mileage"]
    quality = player["shoe_quality"]
    #how long each tier of model lasts
    if quality == "Budget":
        shoe_threshold = 300
    elif quality == "Mid Range":
        shoe_threshold= 400
    elif quality == "High End":
        shoe_threshold = 500
    else:
        shoe_threshold = 350 #default threshold for unknown quality

    ratio = mileage / shoe_threshold #how worn the shoes are

    if ratio >= 1.0:
        print("Your shoes are completely worn out! You need to buy a new pair to continue training.")
        player["health"] -= 20
    elif ratio >= 0.75:
        print("Your shoes are very worn out. You should consider buying a new pair soon.")
        player["health"] -= 10
    elif ratio >= 0.5:
        print("Your shoes are getting worn out. You should start thinking about buying a new pair.")
        player["health"] -= 5
    else:
        print("Your shoes are in good condition. Keep up the good work!")
    player["health"] = max(0, player["health"])














"""Injury Checker"""
def injury_check():
    clear_screen()
    print("Injury Update: ")
    if player["health"] <= 20:
        chance = 0.8  # 80% chance of injury
    elif player["health"] <= 40:
        chance = 0.4  # 40% chance
    elif player["health"] <= 60:
        chance = 0.1  # 10% chance
    else:
        chance = 0.0  # no chance

    if random.random() < chance:
        severity = random.randint(5, 20)
        player["health"] -= severity
        player["health"] = max(0, player["health"])
        print(f"You got injured! You lost {severity} health.")
        if player["health"] == 0:
            print("Your health has hit 0. You are out for the season!")
    else:
        print("No injuries this week.")
    input("Press Enter To Continue")
