


def qualify_for_next(event_name, position,):
    if event_name == "Districts":
        cutoff = 5  # top 5 advance to regions
    elif event_name == "Regions":
        cutoff = 3   # top 3 advance to states
    else:
        return True  # states is the final race, no advancing

    if position <= cutoff:
        print(f"Congratulations! You qualified for the next round by finishing in position {position} at {event_name}!")
        return True
    else:
        print(f"Unfortunately, you did not qualify for the next round. You finished in position {position} at {event_name}.")
        return False


def season_recap():
    print("Season recap to be added next")