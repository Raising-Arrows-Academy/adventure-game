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
            "description": "You are in a dark dungeon cell. There is a door to the NORTH.",
            "north": "hallway",
        },
        "hallway": {
            "description": "You are in a castle hallway.  Torches flicker on the walls.\nThere is a door to the SOUTH and another to the NORTH.",
            "south": "dungeon",
            "north": "courtyard",
        },
        "courtyard": {
            "description": "You are in the castle courtyard!  You can see the exit to NORTH.\nFreedom is so close!",
            "south": "hallway",
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

        elif command in ["north", "south", "east", "west", "n", "s", "e", "w"]:
            # Convert short versions to full directions
            if command == "n":
                command = "north"
            elif command == "s":
                command = "south"
            elif command == "e":
                command = "east"
            elif command == "w":
                command = "west"

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
