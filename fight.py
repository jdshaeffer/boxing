# prototype - fight_turn_based.py is the current implementation

from random import randint
from time import sleep
import threading
import os, select
import time
import sys

class player():
    def __init__(self, level, hp, xp, stam):
        self.level = level
        self.hp = hp
        self.xp = xp
        self.stam = stam
    def r_hook(self, enemy):
        enemy.hp = enemy.hp - 2
        print('Opponent hp: ', enemy.hp, '\n')
    def l_hook(self, enemy):
        enemy.hp = enemy.hp - 2
        print('Opponent hp: ', enemy.hp, '\n')
    def r_jab(self, enemy):
        enemy.hp = enemy.hp - 1
        print('Opponent hp: ', enemy.hp, '\n')
    def l_jab(self, enemy):
        enemy.hp = enemy.hp - 1
        print('Opponent hp: ', enemy.hp, '\n')
    def uppercut(self, enemy):
        enemy.hp = enemy.hp - 3
        print('Opponent hp: ', enemy.hp, '\n')
    
class enemy():
    def __init__(self, level, hp):
        self.level = level
        self.hp = hp
    def punch(self, player):
        while player.hp > 0:
            if(self.hp > 0):
                print('Your opponent throws a punch.\n') # block left/right eventually
                pow = randint(0, 4) # will change to level based value
                player.hp = player.hp - pow
                sleep(2) # will change to level based value
        print('You fall to the ground.')
        sleep(1)
        print('GAME OVER')
        os._exit(1) # kills thread and main

def print_tutorial():
    print('Your moves:')
    print(' - Right hook: rhook')
    print(' - Left hook: lhook')
    print(' - Right jab: rjab')
    print(' - Left jab: ljab')
    print(' - Uppercut: uppercut')
    print(' - Display this tutorial again: help\n')

if __name__ == '__main__':
    # flags
    start = True
    fight = False

    # game
    ai = enemy(10,10)
    guy = player(10,10,0,10)
    print('You\'re in a boxing ring. There\'s someone in the opposite corner. Fight him?')
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
        x = input('> ')
        if x == 'yes' or x == 'y':
            print('Want to read the tutorial first?')
            tut = input('> ')
            if tut == 'yes' or tut == 'y':
                print_tutorial()
                sleep(5)
            else:
                print('Okay, never mind.\n')
                sleep(1)
            print('DING DING DING\n')
            sleep(1)
            print('A challenger approaches.\n')
            sleep(1)
            print('FIGHT!\n')
            sys.stdout.flush() # flush buffer (accept input only after FIGHT)
            while select.select([sys.stdin.fileno()], [], [], 0.0)[0]:
                os.read(sys.stdin.fileno(), 4096)
            startTime = time.time() # start the timer
            sleep(1)
            fight = True
            start = False
        elif x == 'no' or x == 'n':
            print('You bow out.')
            sleep(1)
            print('The crowd throws tomatoes at you.')
            sleep(1)
            print('GAME OVER\n')
            exit()
        else:
            print('Hm? Speak up son.\n')

    # opponent starts punching
    thread = threading.Thread(target=ai.punch, args=[guy])
    thread.daemon = True
    thread.start()

    while fight:
        if ai.hp > 0:
            x = input()
            if x == 'help':
                print_tutorial()
            elif x == 'rhook':
                guy.r_hook(ai)
            elif x == 'lhook':
                guy.l_hook(ai)
            elif x == 'rjab':
                guy.r_jab(ai)
            elif x == 'ljab':
                guy.l_jab(ai)
            elif x == 'uppercut':
                guy.uppercut(ai)
            else:
                print('What?\n')
        else:
            print('You knock him to the ground.')
            sleep(1)
            print('You win!')
            sleep(1)
            elapsedTime = time.time() - startTime
            print('Final time:', elapsedTime, '\n')
            os._exit(1)
