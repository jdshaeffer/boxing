from time import sleep
import time
import sys, os, select
from enemies.boxer import Boxer
from attack import Attack
from player import Player

def print_tutorial():
    print("here's a tutorial...")

if __name__ == "__main__":
    # flags
    start = True
    fight = False

    # attack creation
    righthook = Attack("righthook", 2)
    lefthook = Attack("lefthook", 2)
    rightjab = Attack("rightjab", 1)
    leftjab = Attack("leftjab", 1)
    attacks = [righthook, lefthook, rightjab, leftjab]

    # character creation
    ai = Boxer(4,13,3) # level 1 ai with hp 13 and speed 3 (level plus 9 = default hp)
    guy = Player(1,10,10,attacks) # default: level 1, hp 10, stamina 10, default moves

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