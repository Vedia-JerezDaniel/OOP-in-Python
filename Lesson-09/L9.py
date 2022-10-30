import random
class Dice:
    def __init__(self):
        self.__sideUp=1
    def roll(self):
        self.__sideUp=random.randint(1,6)
    def __str__(self):
        return str(self.__sideUp)

## Main Program ##
myDice=Dice()

for _ in range(6):
    myDice.roll()
    # myDice.__sideUp=6
    "si es _sideUp se puede modificar, si es __sideUp no se puede modificar"
    print(myDice)
