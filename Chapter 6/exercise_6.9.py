frank = ["china", "japan", "korea"]
eric = ["india", "england"]
joy = ["france"]

favourite_places = {'frank': frank, 'eric': eric, 'joy': joy}

for name, places in sorted(favourite_places.items()):
    locations = ""
    for current in range(0, len(places)):
        if len(places) == 1 or (len(places) == 2 and current == 0):
            locations = sorted(places)[current].title()
            if len(places) == 2:
                locations += " "
        elif current == len(places) - 1:
            locations += "and " + sorted(places)[current].title() + "."
        else:
            locations += sorted(places)[current].title() + ", "
    if len(places) == 1:
        print(f"{name.title()}'s favourite place is {locations}")
    else:
        print(f"{name.title()}'s favourite places are {locations}")
