from functions import clear_screen
from save_system import save_game
from player import player
from postseason import qualify_for_next, season_recap




"""Game Loop"""
def game_loop():
    while True:
        clear_screen()
        print("\n===== WEEK", player["week"], "=====")
        #printing each of the options in the general gameplay menu
        print("1. Status")
        print("2. Set Training Plan")
        print("3. Store")
        print("4. Schedule")
        print("5. Upgrade")
        print("6. Advance to next week")
        print("7. Save Game")
        print("8. Exit Game")

        choice = input(">")
        #taking the user to their choice
        if choice == "1":
            from menus import status_menu
            status_menu()
        elif choice == "2":
            from menus import training_plan_menu
            training_plan_menu()
        elif choice == "3":
            from store import store_menu
            store_menu()
        elif choice == "4":
            from schedule import display_schedule
            display_schedule(player["schedule"], player["week"])
        elif choice == "5":
            from menus import upgrade_menu
            upgrade_menu()
        elif choice == "6":
            from functions import update_fitness, health_update, fitness_update, experience_gained, injury_check, shoe_check
            from races import run_race


            clear_screen()
            #all end of the week updates are here, injuries and changes to stats
            update_fitness(player["weekly_mileage"])
            health_update()
            fitness_update(player["weekly_mileage"])
            experience_gained()
            injury_check()
            shoe_check()
            clear_screen()
            print("Advancing to next week. . .")
            player["week"] += 1
            player["money"] += 25


            current_event = player["schedule"].get(str(player["week"])) #Checking to see if there is a race this week, and if there is it will take the player to that race
            if current_event and current_event["type"] == "meet":
                print(f"*** MEET THIS WEEK: {current_event['name']} ***")
                input("Press Enter to race...")
                run_race(current_event["course"])
            elif current_event and current_event["type"] == "postseason": #checking for postseason events (not added yet)
                print(f"*** {current_event['name']} THIS WEEK ***")
                input("Press Enter to continue...")
                position = run_race(current_event["course"])
                advances = qualify_for_next(current_event, position)
                if not advances:
                    season_recap()

            input("Press Enter to continue...")
        elif choice == "7":
            save_game()
        elif choice == "8":
            from menus import main_menu
            main_menu()
            break
        else:
            print("Invalid choice. Please try again.")
