# dialogue/conversation:
    # important to not break immersion - timer element
    # speak freely, get interpreted
    # based on what npc interprets, perception of user will change - outcome of game can change
    # remember: string data types are immutable in python
    # talk however you want - get robust responses

class NPC():
    def __init__(self, name, description, location, is_talking):
        self.name = name
        self.description = description
        self.location = location
        self.is_talking = is_talking

greetings = ["hello","hi"]
goodbyes = ["bye","later"]

class Player():
    def __init__(self, inv, location):
        self.inv = inv
        self.location = location

    def talk_to(self, npc): # needs to be member of Player?
        while 1:
            x = input("--> ")
            for i in range(len(greetings)):
                if greetings[i] in x.lower():
                    print("\tsup dood")
            for i in range(len(goodbyes)):
                if goodbyes[i] in x.lower():
                    print("\tk bye")


if __name__ == "__main__":
    user = Player([],"")
    npc = NPC("","","",False)

    user.talk_to(npc)