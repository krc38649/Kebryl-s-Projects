import random
from courses import courses

POSTSEASON = [
    {"name": "Districts", "week": None},
    {"name": "Regions", "week": None},
    {"name": "States", "week": None},
]

def generate_schedule(total_weeks=25, num_meets=random.randint(5, 8)):
    schedule = {}

    #Last three weeks for postseason meets
    postseason_start = total_weeks - 2
    available_weeks = list(range(3, postseason_start)) #meets start after week 3, do not overlap with postseason

    #randomly but evenly distribute meets across the season
    meet_weeks = sorted(random.sample(available_weeks, num_meets)) #assigned what weeks are meets

    course_names = list(courses.keys())

    for week in range(1, total_weeks+1): #assignes courses to a certain meet week
        if week in meet_weeks:
            course = random.choice(course_names)
            schedule[str(week)] = {"type": "meet",
                              "name": f"{course} Invitational",
                                "course": course}
        elif week == postseason_start:
            schedule[str(week)] = {"type": "postseason", "name": "Districts" , "course": "Districts"}
        elif week == postseason_start + 1:
            schedule[str(week)] = {"type": "postseason", "name": "Regions" , "course": "Regions"}
        elif week == postseason_start + 2:
            schedule[str(week)] = {"type": "postseason", "name": "States" , "course": "States"}
        else:
            schedule[str(week)] = {"type": "training"}

    return schedule


"""function to print the schedule in a nice format"""
def display_schedule(schedule, current_week):
    tag = ""
    from functions import clear_screen
    clear_screen()
    print("===== SEASON SCHEDULE =====")
    for week, event in schedule.items():
        if event["type"] == "training":
            tag = "Training Week"
        elif event["type"] == "meet":
            tag = f"Meet - {event['name']}"
        elif event["type"] == "postseason":
            tag = f" *** POSTSEASON - {event['name']} ***"

        marker = "<---------YOU ARE HERE" if int(week) == current_week else ""
        print(f"Week {week:>2}: {tag}{marker}")

    from functions import return_to_menu
    return_to_menu()