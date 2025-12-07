"""
ADVENTURE GAME LAUNCHER
Created with AI assistance for Python learning

Select and play different adventure games!
"""



def show_game_menu():
    """Display available adventure games"""
    print("\n" + "=" * 50)
    print("ADVENTURE GAME COLLECTION")
    print("=" * 50)
    print("\nAvailable Games:")
    print("  1. Castle Escape - Escape from a mysterious castle!")
    print("  q. Quit")
    print()


def launch_castle_escape():
    """Launch the Castle Escape game"""
    # Import and run the castle escape game
    from castle_escape import castle_escape

    castle_escape.main()


def main():
    """Main launcher function"""

    # Dictionary of available games
    games = {"1": {"name": "Castle Escape", "function": launch_castle_escape}}

    while True:
        show_game_menu()
        choice = input("Select a game (enter number): ").strip().lower()

        if choice in ["q", "quit", "exit"]:
            print("\nThanks for playing! Goodbye!")
            break

        elif choice in games:
            print(f"\nLaunching {games[choice]['name']}...\n")
            games[choice]["function"]()
            # After game ends, show menu again

        else:
            print("\nInvalid selection. Please try again.")


# This starts the launcher when you run the file
if __name__ == "__main__":
    main()
