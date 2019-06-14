import select, sys
from random import randint
from time import sleep
from attack import Attack

# enemy attacks # NOTE: necessary to be instance of class because of examine command
# each enemy will have its own class (no Enemy class) because of specific defense commands (see punch() below)
# Boxers, for example, can be different levels, just like any other enemy
lowpunch = Attack("low punch", 3, "he goes for your gut - use `block low` to avoid damage")
highpunch = Attack("high punch", 4, "tries to sock you in the face - best to `duck` or `block high`")
righthandpunch = Attack("right hand punch", 3, "comes with his right fist to your left side - use `block left` or `dodge right`")
lefthandpunch = Attack("left hand punch", 3, "he'll go with his left hand to your right side - use `block right` or `dodge left`")
attacks = [lowpunch, highpunch, righthandpunch, lefthandpunch]

class Boxer():
    def __init__(self, level, hp, speed):
        self.level = level
        self.hp = hp
        self.speed = speed
        self.attacks = attacks

    def successful_hit(self, player, whichpunch): # save some lines with this
        print("He hits you.")
        pow = randint(self.attacks[whichpunch].pow, self.level)
        player.hp = player.hp - pow

    def punch(self, player):
        whichpunch = randint(0, len(self.attacks)-1)
        print("He throws a " + self.attacks[whichpunch].name + ".\n\n> ", end = "")
        i, o, e = select.select([sys.stdin], [], [], self.speed) # ignore pylint here
        print()
        if i:
            # like in undertale - lots of custom commands for every enemy
            x = sys.stdin.readline().strip()
            if whichpunch == 0: # lowpunch
                if x == "block low":
                    print("You block his attack.")
                else:
                    self.successful_hit(player, whichpunch)
            elif whichpunch == 1: # highpunch
                if x == "duck":
                    print("He misses.")
                elif x == "block high":
                    print("You block his attack.")
                else:
                    self.successful_hit(player, whichpunch)
            elif whichpunch == 2: # righthandpunch
                if x == "block left":
                    print("You block his attack.")
                elif x == "dodge right":
                    print("You dodge his attack.")
                else:
                    self.successful_hit(player, whichpunch)
            elif whichpunch == 3: # lefthandpunch
                if x == "block right":
                    print("You block his attack.")
                elif x == "dodge left":
                    print("You dodge his attack.")
                else:
                    self.successful_hit(player, whichpunch)
        else:
            print("\nHe hits you.")
            pow = randint(2, self.level)
            player.hp = player.hp - pow
        sleep(1)
    
    def show_enemy_hp(self):
        print("    +", end="") # 4 spaces
        for _ in range(self.level+9):
            print("-", end="")
        print("+")
        print("    |", end="") # 4 spaces
        for _ in range(self.hp):
            print("#", end="")
        for _ in range((self.level+9)-self.hp):
            print(" ", end="")
        print("| ",self.hp,"/",self.level+9," (enemy hp)")
        print("    +", end="") # 4 spaces
        for _ in range(self.level+9):
            print("-", end="")
        print("+")
    # def block(self, player):