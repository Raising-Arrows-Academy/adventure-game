"""
CASTLE ESCAPE - A Text Adventure Game
Created with AI assistance for Python learning

You wake up in a dungeon and must escape the castle!
"""

import random


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
    print("\n--- COMBAT COMMANDS (during battle) ---")
    print("  attack - Attack with your equipped weapon")
    print("  dodge - Try to avoid the enemy's next attack")
    print("  heal - Use health items during battle")
    print("  poison - Use a poison potion on the enemy")
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


def get_weapon_damage(weapon, abilities):
    """Calculate damage based on weapon type and abilities"""
    # Base damage for each weapon
    weapon_damage = {
        "sword": 2,
        "crossbow": 3,
        "spear": 2,
        "mace": 3,
        "knife": 1,
        "stone": 1,
    }

    damage = weapon_damage.get(weapon, 0)

    # Strength ability adds extra damage
    if "strength" in abilities:
        damage += 1

    return damage


def battle(
    opponent_name, opponent_health, player_health, inventory, abilities, max_health
):
    """Combat system - player fights an opponent"""
    print("\n" + "=" * 50)
    print(f"⚔️  BATTLE: {opponent_name.upper()} ⚔️")
    print("=" * 50)
    print(f"\nA {opponent_name} blocks your path!")

    # Check if player has a weapon
    weapons = ["sword", "crossbow", "spear", "mace", "knife", "stone"]
    player_weapons = [item for item in inventory if item in weapons]

    if not player_weapons:
        print("\nYou have no weapons to fight with!")
        print(f"The {opponent_name} attacks you mercilessly!")
        return player_health - 2  # Take damage for having no weapon

    # Use the best weapon available
    current_weapon = player_weapons[0]

    # Battle loop
    while opponent_health > 0 and player_health > 0:
        # Show battle status
        print("\n" + "-" * 50)
        print(f"{opponent_name.upper()}: {'❤️' * opponent_health}")
        print(f"YOU: {'❤️' * player_health}")
        print(f"Weapon: {current_weapon}")
        print("-" * 50)

        # Player's turn
        print("\nYour turn! Choose an action:")
        print("  [1] Attack")
        print("  [2] Dodge")
        print("  [3] Heal (use health item)")
        print("  [4] Poison (use poison potion)")

        choice = input("\nEnter your choice (1-4): ").strip()

        player_dodging = False

        if choice == "1":  # Attack
            damage = get_weapon_damage(current_weapon, abilities)
            opponent_health -= damage
            print(f"\nYou attack with your {current_weapon}! -{damage} damage")
            if opponent_health <= 0:
                print(f"\n🎉 Victory! You defeated the {opponent_name}!")
                break

        elif choice == "2":  # Dodge
            player_dodging = True
            print("\nYou prepare to dodge the next attack!")

        elif choice == "3":  # Heal
            # Check for healing items
            healing_items = ["apple", "bread", "elixir"]
            player_healing = [item for item in inventory if item in healing_items]

            if player_healing:
                heal_item = player_healing[0]
                if heal_item == "apple":
                    heal_amount = 2
                elif heal_item == "bread":
                    heal_amount = 1
                elif heal_item == "elixir":
                    heal_amount = 3

                player_health = min(player_health + heal_amount, max_health)
                inventory.remove(heal_item)
                print(f"\nYou use {heal_item}! +{heal_amount} health")
            else:
                print("\nYou have no healing items!")
                print("You lose your turn...")

        elif choice == "4":  # Poison
            if "poison potion" in inventory:
                opponent_health -= 2
                inventory.remove("poison potion")
                print(
                    "\nYou throw a poison potion! The enemy takes -2 damage and is poisoned!"
                )
                if opponent_health <= 0:
                    print(f"\n🎉 Victory! You defeated the {opponent_name}!")
                    break
            else:
                print("\nYou don't have a poison potion!")
                print("You lose your turn...")

        else:
            print("\nInvalid choice! You hesitate and lose your turn!")

        # Check if opponent is defeated
        if opponent_health <= 0:
            break

        # Opponent's turn
        opponent_action = random.choice(
            ["attack", "attack", "dodge"]
        )  # More likely to attack

        if opponent_action == "attack":
            if player_dodging:
                print(f"\nThe {opponent_name} attacks but you dodge!")
            else:
                damage = random.randint(1, 2)  # Opponent does 1-2 damage
                player_health -= damage
                print(f"\nThe {opponent_name} attacks you! -{damage} damage")
        else:
            print(f"\nThe {opponent_name} dodges and prepares to counter!")

    print("\n" + "=" * 50)
    print("Battle Over!")
    print("=" * 50)

    return player_health


def check_for_encounter(current_room, rooms_cleared):
    """Check if player encounters an enemy in this room"""
    # Define which rooms have enemies
    enemy_rooms = {
        "hallway": {"name": "king guard", "health": 3},
        "kitchen": {"name": "kitchen chef", "health": 3},
        "dining_hall": {"name": "servant", "health": 3},
        "throne_room": {"name": "king guard", "health": 3},
    }

    # Check if this room has an enemy and hasn't been cleared
    if current_room in enemy_rooms and current_room not in rooms_cleared:
        return enemy_rooms[current_room]

    return None


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
        "dungeon": ["bread", "stone"],
        "weapon_room": [
            "sword",
            "armor",
            "strength elixir",
            "crossbow",
            "mace",
            "poison potion",
        ],
        "kitchen": ["apple", "bread", "knife"],
        "dining_hall": ["apple", "elixir"],
        "chamber_room": ["invisibility potion", "spear", "poison potion"],
        "courtyard": ["stealth cloak"],
    }

    # Player stats
    health = 5  # Start with 5 hearts
    max_health = 5  # Maximum health
    inventory = []  # Items the player is carrying
    abilities = {}  # Active abilities with turn counters
    rooms_cleared = []  # Track which rooms have been cleared of enemies

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

                # Check for enemy encounters
                encounter = check_for_encounter(current_room, rooms_cleared)
                if encounter:
                    health = battle(
                        encounter["name"],
                        encounter["health"],
                        health,
                        inventory,
                        abilities,
                        max_health,
                    )
                    rooms_cleared.append(current_room)  # Mark room as cleared
                    show_status(health, max_health)

                # Check for traps in the new room
                old_health = health
                health = check_for_trap(current_room, health, abilities)

                # Show health status if it changed
                if health != old_health:
                    show_status(health, max_health)  # Check if player died
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
                    rooms_cleared = []
                    # Refill room items
                    room_items = {
                        "dungeon": ["bread", "stone"],
                        "weapon_room": [
                            "sword",
                            "armor",
                            "strength elixir",
                            "crossbow",
                            "mace",
                            "poison potion",
                        ],
                        "kitchen": ["apple", "bread", "knife"],
                        "dining_hall": ["apple", "elixir"],
                        "chamber_room": [
                            "invisibility potion",
                            "spear",
                            "poison potion",
                        ],
                        "courtyard": ["stealth cloak"],
                    }
                    show_status(health, max_health)
                    show_room(current_room, rooms, room_items)
            else:
                print("\nYou can't go that way!")

        else:
            print("\nI don't understand that command.  Type 'help' for options.")
            # Random chance to encounter a thief when making invalid moves
            if random.randint(1, 100) <= 20:  # 20% chance
                print("\nWhile you're confused, a thief appears!")
                health = battle("thief", 3, health, inventory, abilities, max_health)
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
                    rooms_cleared = []
                    # Refill room items
                    room_items = {
                        "dungeon": ["bread", "stone"],
                        "weapon_room": [
                            "sword",
                            "armor",
                            "strength elixir",
                            "crossbow",
                            "mace",
                            "poison potion",
                        ],
                        "kitchen": ["apple", "bread", "knife"],
                        "dining_hall": ["apple", "elixir"],
                        "chamber_room": [
                            "invisibility potion",
                            "spear",
                            "poison potion",
                        ],
                        "courtyard": ["stealth cloak"],
                    }
                    show_status(health, max_health)
                    show_room(current_room, rooms, room_items)


# This starts the game when you run the file
if __name__ == "__main__":
    main()
