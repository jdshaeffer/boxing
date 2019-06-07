from random import randint
from time import sleep
import threading
import os

class player():
    def __init__(self, level, hp, xp):
        self.level = level
        self.hp = hp
        self.xp = xp

class enemy():
    def __init__(self, level, hp):
        self.level = level
        self.hp = hp
    def punch(self, player):
        while player.hp > 0:
            print("Your opponent throws a punch.\n") # block left/right eventually
            pow = randint(0, 8) # will change to level based value
            player.hp = player.hp - pow
            sleep(2) # will change to level based value
        print("You fall to the ground.")
        sleep(1)
        print("GAME OVER")
        os._exit(1) # kills the whole program (thread and main)

if __name__ == "__main__":
    # flags
    start = True
    fight = False

    # game
    ai = enemy(10,10)
    guy = player(10,10,0)
    print("You're in a boxing ring. There's someone in the opposite corner. Fight him?")

    while start:
        x = input("> ")
        if x == "yes" or x == "y":
            print("DING DING DING")
            sleep(1)
            print("FIGHT!")
            sleep(1)
            print("A challenger approaches. Type help for a tutorial.\n")
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

    thread = threading.Thread(target=ai.punch, args=[guy])
    thread.daemon = True
    thread.start()

    while fight:
        x = input()
        if x == "help":
            print("Your opponent will attack until you're on the ground.")
            print("Your moves:")
            print(" - Right hook: `r hook`")
            print(" - Left hook: `l hook`")
            print(" - Right jab: `r jab`")
            print(" - Left jab: `l jab`")
            print(" - Uppercut: `uppercut`")
            print(" - Display your hp: `hp`\n")
        elif x == "hp":
            print("Your hp: ", guy.hp,"\n")
        else:
            print("What?\n")