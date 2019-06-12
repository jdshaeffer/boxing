from random import randint
from time import sleep
import os, select
import time

class player():
    def __init__(self, level, hp, stam):
        self.level = level
        self.hp = hp
        self.stam = stam
    def turn(self, ai):
        while 1:
            print("""
            +------------+------------+
            | (a) attack |  (r) rest  |
            |------------|------------|
            | (i) item   |  (f) flee  |
            +------------+------------+
            """)
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
    def attack(self, ai):
        while 1:
            print("""
            1) right hook
            2) left hook
            3) right jab
            4) left jab
            5) uppercut
            """)
            x = input("> ")
            if x == "1" or x == "right hook":
            elif x == "2" or x == "left hook":
            elif x == "3" or x == "right jab":
            elif x == "4" or x == "left jab":
            elif x == "5" or x == "uppercut":
            else:
                print("I don't know that move.")

    def rest(self):
    def item(self):
    def flee(self):
    
class enemy():
    def __init__(self, level, hp):
        self.level = level
        self.hp = hp
    def punch(self, player):
        print("Your opponent throws a high punch.\n") # randomly or smartly generated high/low/side punches
        sleep(3)
        x = input("> ")
        if x == "duck":
            print("He misses.")
        elif x == "block high":
            print("You block his high punch.")
        else:
            print("He hits you.")
            pow = randint(0, 4) # will change to level based value
            player.hp = player.hp - pow

def print_tutorial():
    print("Your moves:")
    print(" - Right hook: rhook")
    print(" - Left hook: lhook")
    print(" - Right jab: rjab")
    print(" - Left jab: ljab")
    print(" - Uppercut: uppercut")
    print(" - Display this tutorial again: help\n")

if __name__ == "__main__":
    # flags
    start = True
    fight = False

    # game
    ai = enemy(10,10)
    guy = player(10,10,10)
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
