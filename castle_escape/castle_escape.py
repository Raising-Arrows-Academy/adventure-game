"""
CASTLE ESCAPE - A Text Adventure Game
Created with AI assistance for Python learning

You wake up in a dungeon and must escape the castle!
"""


def show_intro():
    """Display the game introduction"""
    print("\n" + "=" * 50)
    print("CASTLE ESCAPE")
    print("=" * 50)
    print("\nYou wake up in a dark, damp dungeon cell.")
    print("You must find your way out of the castle to freedom!")
    print("\nType 'help' for a list of commands.\n")


def show_help():
    """Show available commands to the player"""
    print("\n--- AVAILABLE COMMANDS ---")
    print("  north, south, east, west - Move in that direction")
    print("  up, down - Go up or down stairs")
    print("  look - Look around the current room")
    print("  help - Show this help message")
    print("  quit - Exit the game")
    print()


def show_room(current_room, rooms):
    """Display the description of the current room"""
    print("\n" + "-" * 50)
    print(rooms[current_room]["description"])
    print("-" * 50)


def main():
    """Main game function - this runs the game!"""

    # Define all the rooms in our castle
    # Each room has a description and exits (which direction leads where)
    rooms = {
        "dungeon": {
            "description": "You are in a dark dungeon cell. Water drips from the ceiling.\nThere is a heavy wooden door to the NORTH.",
            "north": "hallway",
        },
        "hallway": {
            "description": "You are in a dimly lit castle hallway. Torches flicker on the walls.\nYou can go SOUTH to the dungeon, NORTH to the kitchen, or EAST to the weapon room.",
            "south": "dungeon",
            "north": "kitchen",
            "east": "weapon_room",
        },
        "weapon_room": {
            "description": "You are in the weapon room. Swords, shields, and armor hang on the walls.\nThe air smells of metal and oil. You can go WEST back to the hallway.",
            "west": "hallway",
        },
        "kitchen": {
            "description": "You are in the castle kitchen. Old pots and pans hang from hooks.\nA cold fireplace sits in the corner. You can go SOUTH to the hallway,\nEAST to the dining hall, or UP the stairs.",
            "south": "hallway",
            "east": "dining_hall",
            "up": "chamber_room",
        },
        "dining_hall": {
            "description": "You are in the grand dining hall. A long wooden table stretches across the room.\nDusty goblets and plates sit untouched. You can go WEST to the kitchen\nor NORTH to the throne room.",
            "west": "kitchen",
            "north": "throne_room",
        },
        "throne_room": {
            "description": "You are in the magnificent throne room. A golden throne sits on a raised platform.\nRed velvet curtains hang from the tall windows. You can go SOUTH to the dining hall\nor EAST to the courtyard.",
            "south": "dining_hall",
            "east": "courtyard",
        },
        "chamber_room": {
            "description": "You are in a private chamber room. A dusty bed sits against the wall.\nOld paintings hang crookedly. You can go DOWN the stairs back to the kitchen.",
            "down": "kitchen",
        },
        "courtyard": {
            "description": "You are in the castle courtyard! Fresh air fills your lungs.\nYou can see the drawbridge to the NORTH leading over the moat.\nThe throne room is to the WEST.",
            "west": "throne_room",
            "north": "moat",
        },
        "moat": {
            "description": "You are at the castle moat. A wooden drawbridge stretches across murky water.\nYou can see the forest exit to the NORTH - freedom awaits!\nThe courtyard is to the SOUTH.",
            "south": "courtyard",
            "north": "freedom",
        },
    }

    # Game starts in the dungeon
    current_room = "dungeon"

    # Show the introduction
    show_intro()
    show_room(current_room, rooms)

    # Main game loop - keeps running until player quits or wins
    while True:
        # Get command from player
        command = input("\nWhat do you want to do? > ").lower().strip()

        # Handle different commands
        if command in ["quit", "exit", "q"]:
            print("\nThanks for playing!  Goodbye!")
            break

        elif command == "help":
            show_help()

        elif command == "look":
            show_room(current_room, rooms)

        elif command in [
            "north",
            "south",
            "east",
            "west",
            "up",
            "down",
            "n",
            "s",
            "e",
            "w",
            "u",
            "d",
        ]:
            # Convert short versions to full directions
            if command == "n":
                command = "north"
            elif command == "s":
                command = "south"
            elif command == "e":
                command = "east"
            elif command == "w":
                command = "west"
            elif command == "u":
                command = "up"
            elif command == "d":
                command = "down"

            # Check if we can go that direction from current room
            if command in rooms[current_room]:
                next_room = rooms[current_room][command]

                # Check for win condition!
                if next_room == "freedom":
                    print("\n" + "=" * 50)
                    print("🎉 CONGRATULATIONS! 🎉")
                    print("You escaped the castle!")
                    print("YOU WIN!")
                    print("=" * 50)
                    break

                # Move to the next room
                current_room = next_room
                show_room(current_room, rooms)
            else:
                print("\nYou can't go that way!")

        else:
            print("\nI don't understand that command.  Type 'help' for options.")


# This starts the game when you run the file
if __name__ == "__main__":
    main()
