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
        # that way, better for functions - if npc.current_room = self.current_room ... MAYBE NOT BOOLS
        # self can have a current room as well... great for boiler plate...
        # no navigating with bools???

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

class Person():
    def __init__(self, inv, location):
        self.inv = inv
        self.location = location

class Room():
    def __init__(self, description, inv):
        self.description = description
        self.inv = inv

class NPC():
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.current_room = location

# def npc_move():


def look(room_description, room_inv):
    print(room_description)
    print_room_inv(room_inv)

def print_global_commands(input, room_description, room_inv, inv):
    if input == "l":
        look(room_description, room_inv)
    elif input == "i":
        print_personal_inv(inv)
    elif input[:5] == "take ":
        thing = input[5:]
        take(thing,room_inv,inv)
    elif input[:5] == "drop ":
        thing = input[5:]
        drop(thing,room_inv,inv)

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
        print()
    else:
        print("There's nothing here.\n")

def print_personal_inv(inv):
    if len(inv) > 0:
        print("You have:")
        for i in range(len(inv)):
            print("- " + inv[i])
        print()
    else:
        print("You don't have anything.\n")

if __name__ == "__main__":
    # room flags
    red_room = True
    blue_room = False
    green_room = False
    yellow_room = False

    # rooms
    red_room = Room("You're in the red room.",["apple","watermelon"])
    blue_room = Room("You're in the blue room.",["blueberry","fig"])
    green_room = Room("You're in the green room.",["lime","grape"])
    yellow_room = Room("You're in the yellow room.",["lemon","mango"])

    # guy
    guy = Person([], red_room)

    # defaults
    global_commands = ["l", "i", "take ", "drop "]

    # npc
    girl = Person([], yellow_room)
    # npc starts moving
    # thread = threading.Thread(target=ai.punch, args=[guy])
    # thread.daemon = True
    # thread.start()
    while 1:
        while guy.location == red_room:
            x = input("> ")
            if x == "e":
                blue_room = True
                red_room = False
                # guy.location = blue_room
            elif x == "s":
                green_room = True
                red_room = False
            elif x in global_commands or x[:5] in global_commands:
                print_global_commands(x, red_room.description, red_room.inv, guy.inv)
            else:
                print("What?\n")

        while blue_room:
            x = input("> ")
            if x == "s":
                yellow_room = True
                blue_room = False
            elif x == "w":
                red_room = True
                blue_room = False
            elif x in global_commands or x[:5] in global_commands:
                print_global_commands(x, blue_room.description, blue_room.inv, guy.inv)
            else:
                print("What?")

        while green_room:
            x = input("> ")
            if x == "n":
                red_room = True
                green_room = False
            elif x == "e":
                yellow_room = True
                green_room = False
            elif x in global_commands or x[:5] in global_commands:
                print_global_commands(x, green_room.description, green_room.inv, guy.inv)   
            else:
                print("What?")

        while yellow_room:
            x = input("> ")
            if x == "w":
                green_room = True
                yellow_room = False
            elif x == "n":
                blue_room = True
                yellow_room = False
            elif x in global_commands or x[:5] in global_commands:
                print_global_commands(x, yellow_room.description, yellow_room.inv, guy.inv)
            else:
                print("What?")
