from time import sleep
import time
import sys, os, select
from enemies.boxer import Boxer
from attack import Attack
from player import Player
import webbrowser

def open_tutorial():
    webbrowser.open("https://github.com/jdshaeffer/boxing/wiki/Tutorial", new=2)

if __name__ == "__main__":
    # flags
    start = True
    fight = False

    # player attack creation # NOTE: this whole thing could be moved to be class specific (like in boxer.py)
    # righthook = Attack("right hook", 2) # append these at level 2
    # lefthook = Attack("left hook", 2)
    rightjab = Attack("right jab", 1, "a strong forward punch with your right hand")
    leftjab = Attack("left jab", 1, "a strong forward punch with your left hand")
    attacks = [rightjab, leftjab]

    # character creation
    ai = Boxer(4,13,4) # level 1 ai with hp 13 and speed 4 (level plus 9 = default hp)
    guy = Player(1,10,10,attacks,[]) # default: level 1, hp 10, stamina 10, default moves

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
                open_tutorial()
                print("Ready to move on?\n")
                while 1:
                    ready = input("> ")
                    if ready == "yes" or ready == "y":
                        print("Okay, good luck.\n")
                        sleep(2)
                        break
                    else:
                        print("Ready now?\n")
            elif tut == "no" or tut == "n":
                print("Okay, good luck.\n")
                sleep(2)
            else:
                print("Never mind. Have fun out there!\n")
                sleep(2)
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
        ai.punch(guy)
        if guy.hp <= 0:
            print("")
            guy.show_hp()
            print("\nYou fall to the ground.")
            sleep(1)
            print("GAME OVER\n")
            fight = False
        else:
            guy.turn(ai)
            if ai.hp <= 0:
                print("\nYou knock him to the ground.")
                sleep(1)
                print("You win!\n")
                sleep(1)
                elapsedTime = time.time() - startTime
                print("Final time:", elapsedTime, "\n")
                fight = False