from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# item dictionary
item = {
    "torch": Item("torch", "Light it on fire to see in the dark."),
    "rock": Item("rock", "It is heavy and sharp. Use it to bash enemies.")
}

# room items
room["foyer"].items.append(item["torch"])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Nodnarb", room['outside'])

print(player.room.name)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(
        "Your current room:", "\n",
        player.room.name, "\n",
        player.room.description
    )

    direction = input(
        "Input a direction \n(N, S, E, W) \n (or press I to check room for items) \n (or B to check your backpack inventory) : ")

    if direction.lower() == 'q':
        break
    elif direction.lower() == 'n':
        if hasattr(player.room, "n_to"):
            player.room = player.room.n_to
        else:
            print(f"A ROOM DOES NOT EXIST IN THAT DIRECTION ({direction}).")
    elif direction.lower() == 's':
        if hasattr(player.room, "s_to"):
            player.room = player.room.s_to
        else:
            print(f"A ROOM DOES NOT EXIST IN THAT DIRECTION ({direction}).")
    elif direction.lower() == 'e':
        if hasattr(player.room, "e_to"):
            player.room = player.room.e_to
        else:
            print(f"A ROOM DOES NOT EXIST IN THAT DIRECTION ({direction}).")
    elif direction.lower() == 'w':
        if hasattr(player.room, "w_to"):
            player.room = player.room.w_to
        else:
            print(f"A ROOM DOES NOT EXIST IN THAT DIRECTION ({direction}).")

    # check = input("TYPE 'i' TO CHECK ROOM FOR ITEMS: ")

    # if check.lower() != "i":
    #     print("YOU DID NOT HIT 'i' !")

    if direction.lower() == "i":
        if len(player.room.items) == 0:
            print("No items found in this room.")
        elif len(player.room.items):
            for i in player.room.items:
                print(
                    f"You found the {i.name}! Item Description: {i.description}. ")

    if direction.lower() == "b":
        if len(player.inventory) == 0:
            print("No items in your inventory.")
        elif len(player.inventory):
            for i in player.inventory:
                print(f"Item: {i.name}, Item Description: {i.description} ")

    if direction.lower()[0:4] == "take":
        words = direction.split()
        for i in player.room.items:
            if words[1] == i.name:
                player.take_item(i)
                player.room.remove_item_from_room(i)
        print(words)
    elif direction.lower()[0:4] == "drop":
        words = direction.split()
        for i in player.inventory:
            if words[1] == i.name:
                player.drop_item(i)
                player.room.add_item_to_room(i)
        print(words)
    print("\n")
