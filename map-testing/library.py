# The Library
# remember - all descriptions must be concise. Short and sweet. Athletic prose. Like Hemingway.
# I'm wondering... If we'll have a map on display for them, should I let them know the exits?
    # would change the dynamic of room descriptions
    # percentage completion of map? That'd be cool. "oh... you've only found 86% of the map."
# adding every nook and cranny according to the maps? Not yet... stick to the main places

from playground import Room

# level 3 (main floor)
atrium_3rd = Room("Atrium - 3rd Floor",
    "You are in a big glass structure. Lots of light is coming in. There's a statue of a boy and girl reading. " +
    "Stairs lead down to floors below. The floor continues south. Exits to west and east.",
    [])
exhibit_hallway_3rd = Room("Exhibit Hallway",
    "This hallway has an art exhibit to the east. Directly across are some elevators. The hallway opens up to the south. " +
    "There's some benches here.",
    [])
exhibit_from_hallway_3rd = Room("Exhibit - off hallway",
    "There's signs around the small room. There's nothing too interesting here to look at.",
    [])
circulation_3rd = Room("Circulation - 3rd Floor",
    "Soft comfy chairs here. A charging station. There are people available at the Circulation desk. " +
    "Stairs go to floors above and below. There's a sign that says Learning Commons to the west.",
    [])

