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
    print("  search - Search the room for items")
    print("  inventory - Check your items and abilities")
    print("  use [item] - Use an item from your inventory")
    print("  help - Show this help message")
    print("  quit - Exit the game")
    print()


def show_status(health, max_health):
    """Display the player's current health"""
    hearts = "❤️" * health
    empty_hearts = "🖤" * (max_health - health)
    print(f"\nHealth: {hearts}{empty_hearts} ({health}/{max_health})")


def show_inventory(inventory, abilities):
    """Display the player's inventory and active abilities"""
    print("\n--- YOUR INVENTORY ---")
    if inventory:
        for item in inventory:
            print(f"  - {item}")
    else:
        print("  (empty)")

    if abilities:
        print("\n--- ACTIVE ABILITIES ---")
        for ability, turns in abilities.items():
            print(f"  - {ability} ({turns} turns remaining)")
    print()


def search_room(current_room, room_items, inventory):
    """Search the current room for items"""
    if current_room in room_items and room_items[current_room]:
        print("\nYou search the room and find:")
        for item in room_items[current_room]:
            print(f"  - {item}")
            inventory.append(item)
        print("\nItems added to your inventory!")
        # Remove items from room after picking them up
        room_items[current_room] = []
    else:
        print("\nYou search the room but find nothing useful.")


def use_item(item_name, inventory, health, max_health, abilities):
    """Use an item from inventory"""
    # Check if player has the item
    if item_name not in inventory:
        print(f"\nYou don't have {item_name} in your inventory.")
        return health

    # Handle different item types
    if item_name == "apple":
        health = min(health + 2, max_health)  # Add 2 hearts, don't go over max
        inventory.remove("apple")
        print("\nYou eat the apple. It's crispy and refreshing! +2 hearts")

    elif item_name == "bread":
        health = min(health + 1, max_health)  # Add 1 heart
        inventory.remove("bread")
        print("\nYou eat the bread. It's a bit stale but filling. +1 heart")

    elif item_name == "elixir":
        health = min(health + 3, max_health)  # Add 3 hearts
        inventory.remove("elixir")
        print("\nYou drink the elixir. Magic energy flows through you! +3 hearts")

    elif item_name == "strength elixir":
        abilities["strength"] = 2  # Lasts 2 turns
        inventory.remove("strength elixir")
        print("\nYou drink the strength elixir. Your muscles bulge with power!")
        print("Strength ability active for 2 turns!")

    elif item_name == "invisibility potion":
        abilities["invisibility"] = 1  # Lasts 1 turn
        inventory.remove("invisibility potion")
        print("\nYou drink the invisibility potion. You fade from sight!")
        print("Invisibility ability active for 1 turn!")

    elif item_name == "stealth cloak":
        abilities["stealth"] = 2  # Lasts 2 turns
        inventory.remove("stealth cloak")
        print("\nYou put on the stealth cloak. You move silently like a shadow!")
        print("Stealth ability active for 2 turns!")

    else:
        print(f"\nYou can't use {item_name} right now.")

    return health


def update_abilities(abilities):
    """Decrease ability turn counters and remove expired abilities"""
    expired = []
    for ability in abilities:
        abilities[ability] -= 1
        if abilities[ability] <= 0:
            expired.append(ability)
            print(f"\nYour {ability} ability has worn off.")

    # Remove expired abilities
    for ability in expired:
        del abilities[ability]


def check_for_trap(current_room, health, abilities):
    """Check if current room has a trap and apply damage"""
    # Define which rooms have traps
    trap_rooms = {
        "hallway": {
            "damage": 1,
            "message": "A loose stone triggers a dart trap! -1 heart",
        },
        "chamber_room": {
            "damage": 2,
            "message": "The floor gives way to spikes below! -2 hearts",
        },
    }

    # Check if room has a trap
    if current_room in trap_rooms:
        # Check if player has abilities that help avoid traps
        if "invisibility" in abilities:
            print(f"\n⚠️  {trap_rooms[current_room]['message']}")
            print("But you're invisible - the trap doesn't detect you!")
            return health
        elif "stealth" in abilities:
            print(f"\n⚠️  {trap_rooms[current_room]['message']}")
            print(
                "But your stealth helps you avoid most of the damage! -1 heart instead"
            )
            return health - 1
        else:
            print(f"\n⚠️  {trap_rooms[current_room]['message']}")
            return health - trap_rooms[current_room]["damage"]

    return health


def show_room(current_room, rooms, room_items):
    """Display the description of the current room"""
    print("\n" + "-" * 50)
    print(rooms[current_room]["description"])

    # Show if there are items in the room
    if current_room in room_items and room_items[current_room]:
        print("\n💡 You notice something here. Try 'search' to look for items.")

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

    # Define items in each room
    room_items = {
        "dungeon": ["bread"],
        "weapon_room": ["sword", "armor", "strength elixir"],
        "kitchen": ["apple", "bread"],
        "dining_hall": ["apple", "elixir"],
        "chamber_room": ["invisibility potion"],
        "courtyard": ["stealth cloak"],
    }

    # Player stats
    health = 5  # Start with 5 hearts
    max_health = 5  # Maximum health
    inventory = []  # Items the player is carrying
    abilities = {}  # Active abilities with turn counters

    # Game starts in the dungeon
    current_room = "dungeon"

    # Show the introduction
    show_intro()
    show_status(health, max_health)
    show_room(current_room, rooms, room_items)

    # Main game loop - keeps running until player quits or wins
    while True:
        # Update abilities (decrease turn counters)
        if abilities:
            update_abilities(abilities)

        # Get command from player
        command = input("\nWhat do you want to do? > ").lower().strip()

        # Handle different commands
        if command in ["quit", "exit", "q"]:
            print("\nThanks for playing!  Goodbye!")
            break

        elif command == "help":
            show_help()

        elif command == "look":
            show_room(current_room, rooms, room_items)

        elif command == "search":
            search_room(current_room, room_items, inventory)

        elif command in ["inventory", "inv", "i"]:
            show_inventory(inventory, abilities)

        elif command.startswith("use "):
            # Extract item name after "use "
            item_name = command[4:].strip()
            health = use_item(item_name, inventory, health, max_health, abilities)
            show_status(health, max_health)

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
                show_room(current_room, rooms, room_items)

                # Check for traps in the new room
                old_health = health
                health = check_for_trap(current_room, health, abilities)

                # Show health status if it changed
                if health != old_health:
                    show_status(health, max_health)

                # Check if player died
                if health <= 0:
                    print("\n" + "=" * 50)
                    print("💀 YOU DIED! 💀")
                    print("Your health has run out.")
                    print("=" * 50)
                    print("\nRestarting game...\n")
                    # Reset to start
                    current_room = "dungeon"
                    health = 5
                    inventory = []
                    abilities = {}
                    # Refill room items
                    room_items = {
                        "dungeon": ["bread"],
                        "weapon_room": ["sword", "armor", "strength elixir"],
                        "kitchen": ["apple", "bread"],
                        "dining_hall": ["apple", "elixir"],
                        "chamber_room": ["invisibility potion"],
                        "courtyard": ["stealth cloak"],
                    }
                    show_status(health, max_health)
                    show_room(current_room, rooms, room_items)
            else:
                print("\nYou can't go that way!")

        else:
            print("\nI don't understand that command.  Type 'help' for options.")


# This starts the game when you run the file
if __name__ == "__main__":
    main()
