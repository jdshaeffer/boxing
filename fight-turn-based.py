from random import randint
from time import sleep
import time
import sys, os, select


class attack(): # similar to a weapons class
    def __init__(self, pow):
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
            x = input("> ")
            if x == "a":
                self.attack(ai)
                break
            elif x == "i":
                self.item()
                break
            elif x == "r":
                self.rest()
                break
            elif x == "f":
                self.flee()
                break
            else:
                print("Sorry, try again.")

    def show_hp(self):
        print("Your hp:")
        print("+", end="")
        for _ in range(self.level):
            print("-", end="")
        print("+")
        print("|",end="")
        for _ in range(self.hp):
            print("#", end="")
        for _ in range(self.level-self.hp):
            print(" ", end="")
        print("| ",self.hp,"/",self.level)
        print("+", end="")
        for _ in range(self.level):
            print("-", end="")
        print("+")

    def attack(self, ai):
        # how to add more moves as the player levels up - list access
        while 1:
            for i in range(len(attacks)):
                print(i + ") " + attacks[i])
            x = input("> ")
            # if x == "1" or x == "right hook":
                
            # elif x == "2" or x == "left hook":
            # elif x == "3" or x == "right jab":
            # elif x == "4" or x == "left jab":
            # elif x == "5" or x == "uppercut":
            # else:
            #     print("I don't know that move.")

    def rest(self):
        print("Resting...")
    def item(self):
        print("item...")
    def flee(self):
        print("fleeing...")
    # def levelup(self, attacks):
    
class enemy():
    def __init__(self, level, hp, speed):
        self.level = level
        self.hp = hp
        self.speed = speed
    def punch(self, player):
        print("He throws a high punch.\n> ", end = "")
        i, o, e = select.select([sys.stdin], [], [], self.speed)
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
        sleep(1)
    
    # def block(self, player):


def print_tutorial():
    print("here's a tutorial...")

if __name__ == "__main__":
    # flags
    start = True
    fight = False

    # object creation
    righthook = attack(2)
    lefthook = attack(2)
    rightjab = attack(1)
    leftjab = attack(1)
    attacks = [righthook, lefthook, rightjab, leftjab]
    ai = enemy(4,10,3)
    guy = player(1,10,10,attacks)

    # execution
    print("You're in a boxing ring. There's someone in the opposite corner. Fight him?")
    print("""
                              /////'
                             '  # o
                             C   - |
                ___          '  =__'        ___
               (` _ \_       |   |        _/  ')
                \  (__\  ,---- _ |----.  /__)- |
                 \__  ( (           /  ) )  __/
                   |_X_\/ \.   #  _.|  \/_X_|
                     |  \ /(   /    /\ /  |
                      \ /  (  ,    /  \ _/
                           /______/
                          [:::::::]
                         /*%*%*%*%*\\
                         >%*%#%*%*%|
                        /%*%*#*%*%*\\
                       ######^######  \n\n\n""")
    
    while start:
        x = input("> ")
        if x == "yes" or x == "y":
            print("Want to read the tutorial first?")
            tut = input("> ")
            if tut == "yes" or tut == "y":
                print_tutorial()
                sleep(5)
            else:
                print("Okay, never mind.\n")
                sleep(1)
            print("DING DING DING\n")
            sleep(1)
            print("A challenger approaches.\n")
            sleep(1)
            print("FIGHT!\n")
            sys.stdout.flush() # flush buffer (accept input only after FIGHT)
            while select.select([sys.stdin.fileno()], [], [], 0.0)[0]:
                os.read(sys.stdin.fileno(), 4096) # thanks to @Kylar from SO for this solution
            startTime = time.time() # start the timer
            sleep(1)
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
            
            # guy.stam = guy.stam + 1 # increment stam by 1 automatically
            # implement stamina later
