

from functions import clear_screen, return_to_menu
from game_loop import game_loop
from save_system import save_game, load_game
from player import player
import os








"""Character Creation"""
def create_character():
    from functions import clear_screen

    clear_screen()

    while True:
        temp_name = input("Enter your character's name: ")
        #making sure the users name is valid
        if temp_name.isalnum() and len(temp_name) <15 and temp_name not in [save[:-5] for save in os.listdir("saves")]:
            player["name"] = temp_name.capitalize()
            break
        else:
            input("Invalid name. Please enter a name that contains only letters and numbers or doesn't have a local save already. Press Enter to try again.")
            clear_screen()

    points = 50
    print("You have 50 points to distribute among your stats:")
    #setting up beginning stats
    while points > 0:
        print("\n Points remaining: ", points)
        print("1. Stamina: ", player["stamina"])
        print("2. Hills: ", player["hills"])
        print("3. Kick: ", player["kick"])


        try:
            choice = input("Chose what stat to increase: ")
            amount = int(input("How many points do you want to add? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


        if amount> points:
            print("You don't have enough points. Please try again.")
            continue

        if choice == "1":
            player ["stamina"] += amount
        elif choice =="2":
            player ["hills"] += amount
        elif choice == "3":
            player ["kick"] += amount
        else:
            print("Invalid choice. Please try again.")
            continue

        points -= amount

    print("\n Congratulations! Your character has been created!! ")
    print(player)
    input("Your parents offer to pay for your first pair of shoes! Press enter to continue. . . . ")


"""Menus"""
def main_menu():
    clear_screen()
    print("Welcome to RunSim!")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Exit")
    print("4. Delete Save")
    print("5. Credits/version")

    choice = input("Enter your choice: ")
    if choice == "1":
        start_new_game()
    elif choice == "2":
        success = load_game()
        if success:
            game_loop()
    elif choice == "3":
        exit()
    elif choice == "4":
        from save_system import delete_save
        delete_save()
    elif choice == "5":
        clear_screen()
        print("*** CREDITS ***")
        print("Runsim was created by Kebryl Chandler, it began as a simple text based project for my python class, but it was too interesting for me to stop developing, so now its a simple game for runners to enjoy")
        print("Shoutout to the many people who helped me with ideas and testing, I really appreciate it!")
        input("\nPress enter to move onto the version info...")
        clear_screen()
        print("*** VERSION INFO ***")
        print("Please note, this game is in very early development, there are many features that I want to add and many bugs (and balancing issues) that I need to fix, but I wanted to share it with people as soon as possible so I can get feedback and ideas for how to make it better!")
        print("Current Version 0.0.1 (FIRST PUBLIC RELEASE!)")
        input("\nPress enter to return to the main menu...")
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        main_menu()


"""Status Menu"""
#displays all info about the current player
def status_menu():
    clear_screen()
    print("\n===== STATUS =====")
    print("Name: ", player["name"])
    print("Health: ", player["health"])
    print("Fitness: ", player["fitness"])
    print("Shoe Mileage: ", player["shoe_mileage"])
    print("Stamina: ", player["stamina"])
    print("Hills: ", player["hills"])
    print("Kick: ", player["kick"])
    print("Money: ", player["money"])
    print("Week: ", player["week"])
    print("Year: ", player["year"])
    print("Weekly Mileage: ", player["weekly_mileage"])
    print("Weekly Intensity: ", player["weekly_intensity"])
    print("Experience Points: ", player["experience_points"])
    print("Shoes: ", player["shoes"])
    print("Shoe Quality: ", player["shoe_quality"])
    return_to_menu()
    return


"""Start New Game"""
#the list of things that happen when a new character is created
def start_new_game():
    from schedule import generate_schedule
    from store import store_menu
    clear_screen()
    create_character()
    """Go to the store menu, if the player doesn't have shoes, they get taken back to the store menu until they buy a pair of shoes."""
    while player["shoes"] == "":
        store_menu()
        if player["shoes"] == "":
            input("You need to buy a pair of shoes to start training! Press enter to return to the store.")
    player["schedule"] = generate_schedule()
    save_game()
    game_loop()


"""Training Plan Menu"""
def training_plan_menu():
    clear_screen()
    print("\n===== TRAINING PLAN =====")
    print("1. Change Weekly Mileage")
    print("2. Change Training Intensity")
    choice = input("Enter your choice: ")
    if choice == "1":
        clear_screen()
        print("CHANGE WEEKLY MILEAGE")
        player["weekly_mileage"] = int(input("Enter new weekly mileage: "))
        if player["weekly_mileage"] < 5 or player["weekly_mileage"] > 100:
            input("Invalid mileage. Please enter a number between 5 and 100. press enter to try again.")
            training_plan_menu()
    elif choice == "2":
        clear_screen()
        print("CHANGE TRAINING INTENSITY")
        print ("1. HARD")
        print ("2. NORMAL")
        print ("3. EASY")
        intensity_choice = input("Enter new training intensity: ")
        if intensity_choice == "1" or intensity_choice.upper == "HARD":
            player["weekly_intensity"] = "Hard"
        elif intensity_choice == "2" or intensity_choice.upper == "NORMAL":
            player["weekly_intensity"] = "Normal"
        elif intensity_choice == "3" or intensity_choice.upper == "EASY":
            player["weekly_intensity"] = "Easy"
        else:
            input("Invalid choice. Please enter 1, 2, or 3. Press enter to try again.")
            training_plan_menu()
    game_loop()

"""UPGRADE MENU"""

def upgrade_menu():
    clear_screen()
    print("\n===== UPGRADE =====")
    print("Experience Points: ", player["experience_points"])
    print("It costs 5 experience points to upgrade each stat one level. Choose wisely!")
    print("1. Upgrade Stamina (5 points)")
    print("2. Upgrade Hills (5 points)")
    print("3. Upgrade Kick (5 points)")
    print("4. Return to Main Menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        if player["experience_points"] >= 5:
            player["stamina"] += 1
            player["experience_points"] -= 5
            print("Stamina upgraded!")
        else:
            input("Not enough experience points. Press enter to return to menu.")
            upgrade_menu()
    elif choice == "2":
        if player["experience_points"] >= 5:
            player["hills"] += 1
            player["experience_points"] -= 5
            print("Hills upgraded!")
        else:
            input("Not enough experience points. Press enter to return to menu.")
            upgrade_menu()
    elif choice == "3":
        if player["experience_points"] >= 5:
            player["kick"] += 1
            player["experience_points"] -= 5
            print("Kick upgraded!")
        else:
            input("Not enough experience points. Press enter to return to menu.")
            upgrade_menu()
    elif choice == "4":
        return
    else:
        input("Invalid choice. Please enter 1, 2, or 3. Press enter to try again.")
        upgrade_menu()
    return_to_menu()



