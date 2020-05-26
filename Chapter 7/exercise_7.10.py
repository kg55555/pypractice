dream_vacation = {}
quit_now = False
while not quit_now:
    name = input("What is your name?\n")
    location = input("What is your dream vacation destination?\n")
    dream_vacation[name] = location
    check = input("Would you like to add another entry?\n")
    if check == 'quit':
        quit_now = True

for name, location in dream_vacation.items():
    print(f"{name.title()} wants to go to {location.title()}")
