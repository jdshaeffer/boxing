import select, sys
from random import randint
from time import sleep

class Boxer():
    def __init__(self, level, hp, speed):
        self.level = level
        self.hp = hp
        self.speed = speed

    def punch(self, player):
        print("He throws a high punch.\n\n> ", end = "")
        i, o, e = select.select([sys.stdin], [], [], self.speed) # ignore pylint here
        print("")
        if i:
            x = sys.stdin.readline().strip()
            if x == "duck":
                print("He misses.")
            elif x == "block high":
                print("You block his attack.")
            else:
                print("He hits you.")
                pow = randint(2, self.level)
                player.hp = player.hp - pow
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