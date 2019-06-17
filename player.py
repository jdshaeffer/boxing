from time import sleep
from random import randint
from attack import Attack

replist = [] # list that keeps track of your moves - should get cleared after every time repeat is found?

class Player():
    def __init__(self, level, hp, stam, attacks, inv):
        self.level = level
        self.hp = hp
        self.stam = stam
        self.attacks = attacks
        self.inv = inv

    def turn(self, ai):
        while 1:
            print("""
    Your turn.
    +---------------+---------------+
    |  (a) attack   |  (e) examine  |
    |---------------|---------------|
    |  (i) item     |  (r) rest     |
    +---------------+---------------+\n""")
            self.show_hp()
            self.show_stam()
            print()
            x = input("> ")
            if x == "a" or x == "attack":
                if self.stam == 0:
                    print("You don't have enough stamina to attack.")
                    sleep(1)
                else:
                    self.attack(ai)
                    break
            elif x == "i" or x == "item":
                self.item()
                break
            elif x == "r" or x == "rest":
                self.rest()
                break
            elif x == "e" or x == "examine":
                self.examine(ai)
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
        if self.hp < 0:
            self.hp = 0
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
            for i in range(len(self.attacks)):
                print(str(i) + ") " + self.attacks[i].name + ": " + self.attacks[i].description)
            print()
            try:
                x = int(input("> "))
                print("\nYou use " + self.attacks[x].name + ".\n")
                sleep(.5)
                replist.append(x)
                if len(replist) != 1:
                    if x == replist[len(replist)-2]: # if the current is equal to the last one
                        print("Your opponent blocks your attack.\n")
                        sleep(1)
                    else:
                        damage = randint(self.attacks[x].pow, self.attacks[x].pow + self.level)
                        ai.hp -= damage
                else:
                    # not too dry here
                    damage = randint(self.attacks[x].pow, self.attacks[x].pow + self.level)
                    ai.hp -= damage
                self.stam -= self.attacks[x].pow
                break
            except (IndexError, ValueError):
                print("Please input a valid number.\n")
            
        ai.show_enemy_hp()
        print()
        sleep(1)

    def rest(self):
        print("You back off for a few seconds.")
        if self.stam < self.level+9: # are stamina and hp going to grow at the same rate when you level up?
            # ^^^ also, remember that (self.level + 9) is total hp and total stamina
            if (self.level+9)-self.stam == 1:
                print("(stamina + 1)")
                self.stam += 1
            else:
                print("(stamina + 2)\n")
                self.stam += 2
        else:
            print("You're already at full stamina.\n")
        sleep(1)

    def item(self):
        if len(self.inv) == 0:
            print("You don't have anything at the moment.\n")
        else:
            for i in range(len(self.inv)):
                print(str(i) + ") " + self.inv[i].name + ": " + self.inv[i].description)
        sleep(1)

    def examine(self, ai):
        print("You stare your opponent down.\n")
        print("His moves:")
        for i in range(len(ai.attacks)): # this is why attacks must be an instance of enemy classes
            print(" - " + ai.attacks[i].name + ": " + ai.attacks[i].description)
        sleep(5) # give some extra time to read
        print()

    # def levelup(self, attacks):