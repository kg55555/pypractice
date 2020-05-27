from random import randint, choice
import string

class Lottery():

    def __init__(self):
        self.winner = self.number_draw()


    def number_draw(self):
        winner = ""
        lottery = [randint(10, 99) for number in range(1, 11)]
        for number in range(1, 6):
            lottery.append(choice(string.ascii_lowercase))
        return lottery

    def chance(self, entry):
        count = 0
        while True:
            winner = ""
            for number in range(1, 5):
                winner += str(choice(self.winner))
            count += 1
            if winner == entry:
                return count

lotto = Lottery()

while True:
    wrong_char = False
    all_num = ''
    for v in lotto.winner:
        all_num += str(v)
    guess = input(f"Today's lottery numbers are: {lotto.winner}\nPlace your bets!\n")
    for index in range(len(guess)):
        if guess[index] not in all_num:
            wrong_char = True
    if wrong_char:
        continue
    print(lotto.chance(guess))





