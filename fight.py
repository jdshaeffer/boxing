from random import randint
from time import sleep

class player():
    def __init__(self, level, hp, xp):
        self.level = level
        self.hp = hp
        self.xp = xp

class enemy():
    def __init__(self, level, hp):
        self.level = level
        self.hp = hp
    def fight(self, player):
        pow = randint(0, self.level)
        # heal = randint(0, self.level // 2)

# start game
start = input("You're in a boxing ring. There's a guy in the opposite corner. Fight him? (y/n)")
if input == "y":
    print("DING DING DING")
    sleep(1)
    print("FIGHT!")
elif input == "n":
    print("WHAT?!")
    sleep(1)
    print("The crowd throws tomatoes at you.")
    sys.exit()
else:
