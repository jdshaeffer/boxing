# script to test inventory dropping and adding - consistent when dropped in a room
# each room has a list of available items - when dropped, if that item is in your inv list, add to room list
# would be nice to have a room class - make objects with descriptions and that list as instances
# for now it'll be ugly with just some random vars
# inv would normally be filled with objects, just strings for now
# look will display room description followed by a listing of all the room's current objects, dunnet style
# each room can have a visit counter - to see how many times you visit a room - good for some flags,
    # including first visit print whole description

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

# rooms
red_room = True
blue_room = False
green_room = False
yellow_room = False

# room inventories
red_room_inv = ["apple"]
blue_room_inv = ["blueberry"]
green_room_inv = ["lime"]
yellow_room_inv = ["lemon"]

# personal inventory
inv = []

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
            print("* " + inv[i])
        print()
    else:
        print("You don't have anything.\n")

if __name__ == "__main__":
    while 1:
        while red_room:
            x = input("> ")
            if x == "e":
                blue_room = True
                red_room = False
            elif x == "s":
                green_room = True
                red_room = False
            elif x == "l":
                print("You're in the red room.")
                print_room_inv(red_room_inv)
            elif x == "i":
                print_personal_inv(inv)
            elif x[:5] == "take ":
                thing = x[5:]
                take(thing,red_room_inv,inv)
            elif x[:5] == "drop ":
                thing = x[5:]
                drop(thing,red_room_inv,inv)
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
            elif x == "l":
                print("You're in the blue room.")
                print_room_inv(blue_room_inv)
            elif x == "i":
                print_personal_inv(inv)
            elif x[:5] == "take ":
                thing = x[5:]
                take(thing,blue_room_inv,inv)
            elif x[:5] == "drop ":
                thing = x[5:]
                drop(thing,blue_room_inv,inv)
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
            elif x == "l":
                print("You're in the green room.")
                print_room_inv(green_room_inv)
            elif x == "i":
                print_personal_inv(inv)
            elif x[:5] == "take ":
                thing = x[5:]
                take(thing,green_room_inv,inv)
            elif x[:5] == "drop ":
                thing = x[5:]
                drop(thing,green_room_inv,inv)   
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
            elif x == "l":
                print("You're in the yellow room.")
                print_room_inv(yellow_room_inv)
            elif x == "i":
                print_personal_inv(inv)
            elif x[:5] == "take ":
                thing = x[5:]
                take(thing,yellow_room_inv,inv)
            elif x[:5] == "drop ":
                thing = x[5:]
                drop(thing,yellow_room_inv,inv)
            else:
                print("What?")
