from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from westdave
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
#player_name = input("What is your name?\n")

#player = player(player_name, room['outside'])

#print(f"\n\nHello {player.name}!\n")

player = Player("Prapti", room["outside"])

# Write a loop that:
#
# * Prints the current room name

print(player.room.name)

# * Prints the current description (the textwrap module might be useful here).

print(player.room.description)

# * Waits for user input and decides what to do.

userInput = input('Input a movement direction (n,w,s,e) press "q" to quit ')
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while userInput != 'q':


    if(userInput not in ['n', 'w', 's', 'e', 'q']):

        userInput = input('please enter valid input press "q" to quit ')

    elif(not hasattr(player.room, f'{userInput}_to') and userInput != 'q'):

        print(userInput)
        userInput = input('you cannot move in that direction: Choose another press "q" to quit ')

    elif(userInput != 'q'):

        player.room = getattr(player.room, f'{userInput}_to')
        print(player.room.name)
        print(player.room.description)

        userInput = input('Input a movement direction (n,w,s,e) press "q" to quit ')

print('done')