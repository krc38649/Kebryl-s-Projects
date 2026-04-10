
import random
from courses import courses
from functions import clear_screen, return_to_menu
from player import player


#RACE SETUP
"""Bonus for nice shoes"""
def get_shoe_modifier():
    quality = player["shoe_quality"]

    if quality == "Budget":
        bonus = 0.0
    elif quality == "Mid Range":
        bonus = 0.1
    elif quality == "High End":
        bonus = 0.2
    else:
        bonus = 0.00 #default if something goes wrong

    # reduce bonus as shoes wear out
    ratio = player["shoe_mileage"] / (300 if quality == "Budget" else 400 if quality == "Mid Range" else 500)
    if ratio >= 0.75:
        bonus = 0.0  # no bonus from worn out shoes

    return bonus



"""How healthy the player is, which effects their performance"""
def get_health_modifier():
    if player["health"] >= 80:
        return 1.0
    elif player["health"] >= 60:
        return 0.85
    elif player["health"] >= 40:
        return 0.70
    elif player["health"] >= 20:
        return 0.50
    else:
        return 0.30

"Formatting the time to make sure it look like 00:00"
def format_time(total_minutes):
    minutes = int(total_minutes)
    seconds = int((total_minutes - minutes) * 60)
    return f"{minutes}:{seconds:02d}"

"""Generating competitors"""
def generate_competitors(num=11):
    competitors = []
    for i in range(num):
        competitors.append({
            "name": f"Runner {i+1}",
            "strength": random.randint (5, 20)
        })

    return competitors
"""Getting the base pace for the player based on their fitness"""

def get_base_pace():
    #lower is faster, fitness brings pace down
    return max(3.0, 7.0 - (player["fitness"] * 0.08)) #calculating what the default pace for each kilometer will be based on the players fitness


"""Race Start"""
def run_race(course_name):
    clear_screen()
    course = courses[course_name]
    profile = course["profile"]
    total_km = len(profile)

    competitors = generate_competitors() #generating competitors
    shoe_mod = get_shoe_modifier() #getting the shoe modifier for the player
    health_mod = get_health_modifier() #getting the health modifier for the player
    stamina = player["stamina"] #stamina pool for the race

    current_stamina = stamina * 3 * health_mod #making the stamina pool a reasonable number
    base_pace = (get_base_pace() / health_mod) - shoe_mod #getting the base pace for the player based on their fitness
    total_time = 0.0 #starting off the time at zero

    print(f"==== RACE: {course_name.title()} ====")
    print(f"Course Description: {course['description']}")
    if player["health"] < 80: #Warning the player if their health is bad before the race
        print(f"\nWarning: You are at {player['health']}/100 health.")
    if player["health"] < 60:
        print("Your performance will be significantly affected.")
    elif player["health"] < 80:
        print("Your performance may be slightly affected.")
    input("\nPress Enter to start the race. . . ")

    #the start line
    clear_screen()
    print("Your on the starting line, how do you want to start this race?")
    print("1. Be Aggressive (High risk, high reward)")
    print("2. Be Conservative (Cautious strategy, less risk)")
    start_choice= input("Choose a starting strategy: ")

    if start_choice == "1":
        position = random.randint(1,len(competitors))
    else:
        position = random.randint(4,8)


    for km in range (1, total_km+1): #for each km in the course profile
        clear_screen()
        hill = profile[km-1] #seeing if there is a hill in that specific km
        is_final_km = km == total_km #checking if it's the final km for a possible kick

        #each kilometer update with useful info
        print(f"==== KM {km} of {total_km} ====")
        print (f"Terrain: {'Flat' if hill == 0 else 'Small Hill' if hill == 1 else 'Big Hill'}")
        print (f"Current Position: {position} / {len(competitors)+1}")
        print (f"Current Stamina: {current_stamina:.1f}")
        print (f"Running Time: {format_time(total_time)}")

    #player decisions during the race
        if is_final_km:
            print("1. Kick Hard (uses all remaining stamina for a boost")
            print("2. Maintain Pace")
        else:
            print("1. Speed up (uses some stamina for a temporary boost)")
            print("2. Maintain Pace (regain a little stamina while not loosing too much ground)")
            print("3. Ease Up (conserve stamina but risk losing position)")
            print("4. Hard Move (uses a lot of stamina for a big boost but risks blowing up)")

        choice = input("\n> ")

        #each km time and changed positions
        km_time = base_pace


        if is_final_km:
            if choice == "1":
                #kicking
                kick_bonus = player["kick"]*0.1
                stamina_bonus = current_stamina * 0.02
                position_change = -int(kick_bonus+stamina_bonus+random.randint(0, 2))
                km_time -= kick_bonus
                current_stamina = 0
            else:
                position_change = random.randint(-2,1)
        else:
            if choice == "1": # Push
                if current_stamina >=15:
                    current_stamina -= 15
                    position_change = -random.randint(0, 2)
                    km_time -=0.2
                else:
                    print("Not enough stamina to push the pace!")
                    position_change = random.randint(-1, 1)
            elif choice == "2": # Maintain Pace
                current_stamina +=5
                position_change = random.randint(-1,1)
            elif choice == "3": #Ease Up
                current_stamina += 15
                position_change = random.randint (-3, 0)
            elif choice == "4": #Hard Move
                if current_stamina >= 25:
                    current_stamina -=25
                    position_change = -random.randint(1,4)
                    km_time -=0.5
                else:
                    print("You do not have enough energy for a hard move! Maintaining pace now!")
                    current_stamina +=5
                    position_change = random.randint (-1,1)
            else:
                print("invalid choice, maintaining pace now")
                current_stamina +=5
                position_change = random.randint (-1,1)

         # HILL EFFECTS
        if hill == 1:
            hill_effect = -(player["hills"] * 0.05)
            position_change += int(hill_effect)
            km_time += 0.3 - (player["hills"] * 0.1)
        elif hill == 2:
            hill_effect = -(player["hills"] * 0.1)
            position_change += int(hill_effect)
            km_time += 0.6 - (player["hills"] * 0.02)

        # slowing down if not enough stamina
        if current_stamina < stamina * 2:
            km_time += 0.3  # fading

        # Clamping the position
        position = max(1, min(len(competitors) + 1, position + position_change))
        total_time += km_time

        print(f"\nKM {km} complete!")
        print(f"Position: {position} / {len(competitors) + 1}")
        print(f"Current Stamina: {current_stamina}")
        if position_change < 0:
            print(f"You moved up {abs(position_change)} place(s)!")
        elif position_change > 0:
            print(f"You dropped {position_change} place(s).")
        else:
            print("You held your position.")

        input("\nPress Enter to continue...")

    clear_screen()
    print("===== RACE COMPLETE =====")
    print(f"Course: {course_name.title()}")
    print(f"Final Position: {position} / {len(competitors) + 1}")
    print(f"Finishing Time: {format_time(total_time)}")

    # Stat gains and rewards based on race performance
    exp_gained = max(1, len(competitors) + 1 - position)
    player["experience_points"] += exp_gained

    if position == 1:
        print("\nYOU WON THE RACE!")
        player["money"] += 100
    elif position <= 3:
        print("\nPodium finish! Great race!")
        player["money"] += 50
    elif position <= 7:
        print("\nSolid race, keep training!")
        player["money"] +=25
    else:
        print("\nTough race. Get back to training.")
        player["money"] +=10

    print(f"\nYou earned {exp_gained} experience points!")
    return_to_menu()
    return position















