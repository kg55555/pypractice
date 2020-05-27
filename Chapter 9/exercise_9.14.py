from random import randint, choice
import string

winner = ""
lottery = [randint(10,99) for number in range(1,11)]
for number in range(1,6):
    lottery.append(choice(string.ascii_lowercase))

for number in range(1,5):
    winner += str(choice(lottery))

print(f"The winning number is {winner}")