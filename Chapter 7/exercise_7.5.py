repeat_age = True
while repeat_age:
    age = int(input("Check your movie ticket price by typing your age below\n"))
    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs $10")
    elif age > 12:
        print("Your ticket costs $15")

    check = input("Would you like to check another ticket price? Type 'quit' to exit this program\n")
    if check == 'quit':
        break
print("Thank you for using our service!")