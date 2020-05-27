from random import randint

class Dice:

    def __init__(self, sides=6):
        self.sides = sides

    def  roll_die(self):
        print(f"\nRolling a {self.sides} sided die")
        for number in range(1,11):
            print(randint(1,self.sides), end=" ")


die6 = Dice()
die10 = Dice(10)
die20 = Dice(20)

die6.roll_die()
die10.roll_die()
die20.roll_die()