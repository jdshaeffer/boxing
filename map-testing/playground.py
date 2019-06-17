# script to test inventory dropping and adding - consistent when dropped in a room vvv
    # each room has a list of available items - when dropped, if that item is in your inv list, add to room list
    # would be nice to have a room class - make objects with descriptions and that list as instances
    # for now it'll be ugly with just some random vars
    # inv would normally be filled with objects, just strings for now
    # look will display room description followed by a listing of all the room's current objects, dunnet style
    # each room can have a visit counter - to see how many times you visit a room - good for some flags,
        # including first visit print whole description
    # will only need to pass in the room object eventually - not its singular attributes

# this script also tests npc movement in the map
    # extend npc class to have a ton of npc_in_room bool values as instances

# map
"""

|--------|--------|
| red    | blue   |
|        |        |
|-----------------|
| green  | yellow |
|        |        |
|--------|--------|

"""
import threading
from random import randint
from time import sleep

class Person():
    def __init__(self, inv, location):
        self.inv = inv
        self.location = location

class Room():
    def __init__(self, name, description, inv):
        self.name = name
        self.description = description
        self.inv = inv

class NPC():
    def __init__(self, name, description, location): # maybe add movement function in the future...
        self.name = name
        self.description = description
        self.location = location


def girl_move(npc, rooms): # probs will be specific to each character
    while 1:
        sleep(5)
        random_room = randint(0, len(rooms)-1)
        npc.location = rooms[random_room]
        print("Ada is in " + npc.location.name)

def check_npcs(guy, npcs):
    for i in range(len(npcs)):
        if guy.location == npcs[i].location:
            print(npcs[i].name + " is here.\n")

def look(room_description, room_inv, guy, npcs):
    print(room_description)
    print_room_inv(room_inv)
    check_npcs(guy, npcs)

def print_global_commands(input, room_description, room_inv, guy, npcs):
    if input == "l":
        look(room_description, room_inv, guy, npcs)
    elif input == "i":
        print_personal_inv(guy.inv)
    elif input[:5] == "take ":
        thing = input[5:]
        take(thing,room_inv,guy.inv)
    elif input[:5] == "drop ":
        thing = input[5:]
        drop(thing,room_inv,guy.inv)

def take(thing, room_inv, inv):
    if thing not in room_inv:
        print("I don't know what you're trying to take.\n")
    else:
        print("You take the " + thing + ".\n")
        inv.append(thing)
        room_inv.remove(thing)

def drop(thing, room_inv, inv):
    if thing not in inv:
        print("I don't know what you're trying to drop.\n")
    else:
        print("You drop the " + thing + ".\n")
        inv.remove(thing)
        room_inv.append(thing)

def print_room_inv(room_inv):
    vowels = ["a","e","i","o","u"]
    if len(room_inv) > 0:
        for i in range(len(room_inv)):
            if room_inv[i][0] not in vowels:
                print("There is a " + room_inv[i] + " here.")
            else:
                print("There is an " + room_inv[i] + " here.")
    else:
        print("There's nothing here.")

def print_personal_inv(inv):
    if len(inv) > 0:
        print("You have:")
        for i in range(len(inv)):
            print("- " + inv[i])
        print()
    else:
        print("You don't have anything.\n")


if __name__ == "__main__":
    # rooms
    red_room = Room("the red room","You're in the red room.",["apple","watermelon"])
    blue_room = Room("the blue room","You're in the blue room.",["blueberry","fig"])
    green_room = Room("the green room","You're in the green room.",["lime","grape"])
    yellow_room = Room("the yellow room","You're in the yellow room.",["lemon","mango"])
    rooms = [red_room, blue_room, green_room, yellow_room]

    # guy
    guy = Person([], red_room)

    # defaults
    global_commands = ["l", "i", "take ", "drop "]

    # npc
    girl = NPC("Ada","She's in Victorian garb.",yellow_room)
    npcs = [girl]


    while 1:
        thread = threading.Thread(target=girl_move, args=[girl, rooms])
        thread.daemon = True
        thread.start()
        while guy.location == red_room:
            x = input("> ")
            if x == "e":
                guy.location = blue_room
            elif x == "s":
                guy.location = green_room
            elif x in global_commands or x[:5] in global_commands:
                print_global_commands(x, red_room.description, red_room.inv, guy, npcs)
            else:
                print("What?\n")

        while guy.location == blue_room:
            x = input("> ")
            if x == "s":
                guy.location = yellow_room
            elif x == "w":
                guy.location = red_room
            elif x in global_commands or x[:5] in global_commands:
                print_global_commands(x, blue_room.description, blue_room.inv, guy, npcs)
            else:
                print("What?\n")

        while guy.location == green_room:
            x = input("> ")
            if x == "n":
                guy.location = red_room
            elif x == "e":
                guy.location = yellow_room
            elif x in global_commands or x[:5] in global_commands:
                print_global_commands(x, green_room.description, green_room.inv, guy, npcs)   
            else:
                print("What?\n")

        while guy.location == yellow_room:
            x = input("> ")
            if x == "w":
                guy.location = green_room
            elif x == "n":
                guy.location = blue_room
            elif x in global_commands or x[:5] in global_commands:
                print_global_commands(x, yellow_room.description, yellow_room.inv, guy, npcs)
            else:
                print("What?\n")
