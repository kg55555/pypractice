quit_now = False
while quit_now == False:
    count = int(input("How many people are in your dinner group?\n"))
    if count <= 20 and count > 0:
        if count > 8:
            print("Sorry, you'll have to wait for a table")
        else:
            print("Perfect! We have a table for you")
    elif count<=0:
        print("Sorry, you have entered an invalid number of people")
    elif count >20:
        print("Sorry, the party is too large, please split it up into multiple reservations")
    response = input("Would you like to make another reservation? type any key to continue and 'n' to quit\n")
    if response.lower() == 'n':
        break
    else:
        continue
print("Thank you for making a reservation with us!")
if count <= 20 and count > 8:
    print("Please wait to be seated")
