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

# flags
start = True
fight = False

# game
enemy = enemy(10,10)
guy = player(10,10,0)
print("You're in a boxing ring. There's a guy in the opposite corner. Fight him? (y/n)")

while start is True:
    x = input("> ") # x is generic var for all input string
    if x is "y":
        print("DING DING DING")
        sleep(1)
        print("FIGHT!")
        sleep(1)
        print("The challenger approaches. Type help for a tutorial.")
        start = False
        fight = True
    elif x is "n":
        print("WHAT?!")
        sleep(1)
        print("The crowd throws tomatoes at you.")
        sleep(1)
        print("THE END")
        exit()
    else:
        print("Hm? Speak up son.\n")

while fight is True:
    if guy.hp == 0:
        print("You fall to the ground.")
        sleep(1)
        print("GAME OVER")
        exit()
    else:
        x = input("> ")
