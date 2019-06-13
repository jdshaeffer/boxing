from random import randint
from time import sleep
import time
import sys, os, select

class attack(): # similar to a weapons class
    def __init__(self, name, pow):
        self.name = name
        self.pow = pow

class player():
    def __init__(self, level, hp, stam, attacks):
        self.level = level
        self.hp = hp
        self.stam = stam
        self.attacks = attacks

    def turn(self, ai):
        while 1:
            print("""
    Your turn.
    +------------+------------+
    | (a) attack |  (r) rest  |
    |------------|------------|
    | (i) item   |  (f) flee  |
    +------------+------------+\n""")
            self.show_hp()
            self.show_stam()
            print("")
            x = input("> ")
            if x == "a" or x == "attack":
                self.attack(ai)
                break
            elif x == "i" or x == "item":
                self.item()
                break
            elif x == "r" or x == "rest":
                self.rest()
                break
            elif x == "f" or x == "flee":
                self.flee()
                break
            else:
                print("Sorry, try again.")

    def show_hp(self):
        print("    +", end="") # 4 spaces
        for _ in range(self.level+9): # level+9 because you start at level 1 with total hp 10
            print("-", end="")
        print("+")
        print("    |",end="") # 4 spaces
        for _ in range(self.hp):
            print("#", end="")
        for _ in range((self.level+9)-self.hp):
            print(" ", end="")
        print("| ",self.hp,"/",self.level+9," (hp)")
        print("    +", end="") # 4 spaces
        for _ in range(self.level+9):
            print("-", end="")
        print("+")

    def show_stam(self):
        print("     ",end="") # 5 spaces
        for _ in range(self.stam):
            print("*", end="")
        for _ in range((self.level+9)-self.stam):
            print(" ", end="")
        print("  ",self.stam,"/",self.level+9," (stamina)")

    def attack(self, ai):
        while 1:
            for i in range(len(attacks)):
                print(str(i) + ") " + attacks[i].name)
            print("")
            try:
                x = int(input("> "))
                print("You use " + attacks[x].name + ".")
                ai.hp -= attacks[x].pow
                self.stam -= attacks[x].pow
                break
            except (IndexError, ValueError):
                print("Please input a valid number.\n")
        sleep(1)

    def rest(self):
        print("You back off for a few seconds.")
        print("(stamina + 2)")
        self.stam += 2
        sleep(1)

    def item(self):
        print("item...")
        sleep(1)

    def flee(self):
        print("fleeing...")
        sleep(1)

    # def levelup(self, attacks):
    
class enemy():
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
    
    # def block(self, player):


def print_tutorial():
    print("here's a tutorial...")

if __name__ == "__main__":
    # flags
    start = True
    fight = False

    # attack creation
    righthook = attack("righthook", 2)
    lefthook = attack("lefthook", 2)
    rightjab = attack("rightjab", 1)
    leftjab = attack("leftjab", 1)
    attacks = [righthook, lefthook, rightjab, leftjab]

    # character creation
    ai = enemy(4,10,3) # level 4 ai with hp 10 and speed 3
    guy = player(1,10,10,attacks) # default: level 1, hp 10, stamina 10, default moves

    # execution
    print("You're in a boxing ring. There's someone in the opposite corner. Fight him?")
    print("""
                              //////
                             |  # o|
                             C   > |
                ___          |  - _/        ___
               (` _ \_       |   |        _/  ')
                \  (__\  ,---- _ |----.  /__)- |
                 \__  ( (           /  ) )  __/
                   |_X_\/ \ .  #  _.|  \/_X_|
                     \  \ /(   /    /\ /  /
                      \__/ (  ,    /  \__/
                           /______/
                          [:::::::]
                         /*%*%*%*%*\\
                         >%*%#%*%*%|
                        /%*%*#*%*%*\\
                       ######^######  \n\n""")
    
    while start:
        x = input("> ")
        if x == "yes" or x == "y":
            print("Want to read the tutorial first?\n")
            tut = input("> ")
            if tut == "yes" or tut == "y":
                print_tutorial()
                sleep(5)
            elif tut == "no" or tut == "n":
                print("Okay, good luck.\n")
                sleep(1)
            else:
                print("Never mind.\n")
                sleep(1)
            print("DING DING DING\n")
            sleep(1)
            print("A challenger approaches.\n")
            sleep(1)
            print("FIGHT!\n")
            sleep(1)
            sys.stdout.flush() # flush buffer (accept input only after FIGHT)
            while select.select([sys.stdin.fileno()], [], [], 0.0)[0]:
                os.read(sys.stdin.fileno(), 4096)
            startTime = time.time() # start the timer
            fight = True
            start = False
        elif x == "no" or x == "n":
            print("You bow out.")
            sleep(1)
            print("The crowd throws tomatoes at you.")
            sleep(1)
            print("GAME OVER\n")
            exit()
        else:
            print("Hm? Speak up son.\n")

    while fight:
        if guy.hp <= 0:
            print("You fall to the ground.")
            sleep(1)
            print("GAME OVER")
            fight = False
        elif ai.hp <= 0:
            print("You knock him to the ground.")
            sleep(1)
            print("You win!")
            sleep(1)
            elapsedTime = time.time() - startTime
            print("Final time:", elapsedTime, "\n")
            fight = False
        else:
            ai.punch(guy)
            guy.turn(ai)