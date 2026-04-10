"""Importing Modules"""
import os
import json
from functions import clear_screen, return_to_menu
from player import player
import sys


#Making a path relative to this file, so it works regardless of where the script is run from
BASE_DIR = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
SAVES_DIR = os.path.join(BASE_DIR, "saves")

if not os.path.exists(SAVES_DIR):
    os.makedirs(SAVES_DIR)


"""Game Save and Load"""




def save_game():
    filename = os.path.join(SAVES_DIR, f"{player['name']}.json")
    clear_screen()
    with open(filename, "w") as save_file:
        json.dump(player, save_file)
    print("Game saved successfully!")
    return_to_menu()


def load_game():
    clear_screen()
    if not os.path.exists(SAVES_DIR):
        os.makedirs(SAVES_DIR)
    saves = [s for s in os.listdir(SAVES_DIR) if s.find(".json") != -1]
    if not saves:
        print("No saves found. Returning to main menu.")
        return_to_menu()
        return False



    print("Select a save to load:\n")
    for i, save in enumerate(saves):
        print(f"{i + 1}. {save.replace(".json", "")}")

    choice = int(input("Choose save >"))
    try:
        selected = saves[int(choice) - 1]
        idx = saves.index(selected)
        filename = os.path.join(SAVES_DIR, saves[idx])
    except (ValueError, IndexError):
        print("invalid choice.")
        return_to_menu()
        return False
    with open (filename, "r") as save_file:
        loaded = json.load(save_file)
        player.update(loaded)

    print(f"\nWelcome back,"+ player['name'])
    return_to_menu()
    return True


def delete_save():
    clear_screen()
    if not os.path.exists(SAVES_DIR):
        os.makedirs(SAVES_DIR)
    saves = os.listdir(SAVES_DIR)
    if not saves:
        print("No saves found. Returning to main menu.")
        return_to_menu()
        return

    print("Select a save to delete:\n")
    for i, save in enumerate(saves):
        print(f"{i + 1}. {save.replace(".json", "")}")

    choice = int(input("Choose save >")) - 1

    confirm = input(f"Are you sure you want to delete the save '{saves[choice][:-5]}'? (y/n) >")
    if confirm.lower() == "y":
        filename = os.path.join(SAVES_DIR, saves[choice])
        os.remove(filename)
        print("Save deleted successfully!")
    else:
        print("Deletion cancelled.")
    return_to_menu()
