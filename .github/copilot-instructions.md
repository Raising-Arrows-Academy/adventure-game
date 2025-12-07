# GitHub Copilot Instructions for Adventure Game Collection

## Project Context

This is an **educational Python project** designed for **high school students who are brand new to programming**. The project uses AI-assisted development as a teaching tool to help students learn Python fundamentals while building text-based adventure games.

## Target Audience

- **Experience Level**: Complete beginners (first programming course)
- **Age Group**: High school students (typically 14-18 years old)
- **Learning Goals**: Python basics, AI literacy, code comprehension, problem-solving

## Code Guidelines

### 1. Keep It Simple - Python Basics Only

**DO** use these fundamental Python concepts:

- ✅ Variables (strings, integers, booleans, lists, dictionaries)
- ✅ Basic control flow (`if`, `elif`, `else`)
- ✅ Loops (`while`, `for`)
- ✅ Functions (simple, well-defined purposes)
- ✅ Built-in functions (`print()`, `input()`, `len()`, `.lower()`, `.strip()`)
- ✅ Dictionary lookups and basic operations
- ✅ String formatting (f-strings are OK if explained)
- ✅ Comments explaining what code does

**AVOID** unless specifically requested:

- ❌ Classes and Object-Oriented Programming (OOP)
- ❌ List comprehensions
- ❌ Lambda functions
- ❌ Decorators
- ❌ Generators
- ❌ Advanced data structures (sets, tuples beyond basics)
- ❌ File I/O (unless specifically needed for save/load features)
- ❌ External libraries beyond standard library
- ❌ Complex error handling (try/except only when essential)
- ❌ Type hints
- ❌ Advanced string methods or regex

### 2. Code Style for Beginners

- **Clarity over cleverness**: Write obvious, readable code
- **Comments**: Add explanatory comments liberally - explain WHY, not just WHAT
- **Variable names**: Use descriptive, full words (e.g., `player_health` not `ph`)
- **Function names**: Action verbs that describe what they do (e.g., `show_room()`, `get_user_command()`)
- **Line length**: Keep lines short and readable
- **Whitespace**: Use blank lines to separate logical sections
- **Consistency**: Follow the existing code style in the project

### 3. Documentation Standards

Every function should have:

- A clear docstring explaining what it does
- Simple, straightforward parameter names
- Obvious return values

Example:

```python
def show_room(current_room, rooms):
    """Display the description of the current room"""
    print("\n" + "-" * 50)
    print(rooms[current_room]["description"])
    print("-" * 50)
```

### 4. Teaching-Focused Code

When adding features:

1. **Break down complexity**: Split large tasks into small, understandable functions
2. **Use clear patterns**: Consistent structure helps students recognize patterns
3. **Add learning comments**: Explain programming concepts as they appear
4. **Test incrementally**: Each feature should be testable independently
5. **Show progression**: Build features that naturally introduce new concepts

Example:

```python
# Main game loop - keeps running until player quits or wins
while True:
    # Get command from player
    command = input("\nWhat do you want to do? > ").lower().strip()

    # Handle different commands
    if command in ["quit", "exit", "q"]:
        print("\nThanks for playing!  Goodbye!")
        break
```

### 5. Feature Implementation

When students suggest features:

- **Start simple**: Implement the most basic version first
- **Use existing patterns**: Follow the established code structure
- **Add gradually**: Don't overwhelm with too many new concepts at once
- **Make it work first**: Get it functional before optimizing

Common student feature requests:

- Inventory system → Use a simple list
- Locked doors → Add key checks to room navigation
- Items → Use dictionaries with item properties
- Health/combat → Simple integer variables and conditionals
- More rooms → Extend the existing rooms dictionary
- NPCs → Simple dialogue with if/elif chains

### 6. Error Handling

- Keep error messages friendly and helpful
- Assume students will make typos and unexpected inputs
- Use simple validation with clear feedback
- Don't crash on bad input - guide users back on track

Example:

```python
else:
    print("\nI don't understand that command. Type 'help' for options.")
```

### 7. Project Structure

Current structure:

```
adventure-game/
├── main.py                  # Game launcher - menu system
├── castle_escape/           # Individual game folders
│   ├── castle_escape.py     # Game logic
│   └── student_handout.md   # Student materials
└── tests/                   # Test files
```

When adding new games:

- Create a new folder for each game
- Follow the `castle_escape` pattern
- Keep game logic self-contained
- Update `main.py` launcher to include new game

### 8. Python Version

- **Target**: Python 3.8+ (common in educational settings)
- **Avoid**: Cutting-edge features that require Python 3.10+
- **Use**: Well-established, stable Python features

### 9. Dependencies

- **Prefer**: Standard library only
- **If needed**: Justify any external dependencies for educational value
- **Document**: Add to `requirements.txt` with explanation

### 10. AI-Assisted Development Principles

This project teaches students how to:

- Work collaboratively with AI
- Review and understand AI-generated code
- Ask clear, specific questions (prompt engineering)
- Think critically about suggested solutions

When generating code:

- Make it a **teaching moment** - code should be readable and educational
- Encourage **iteration** - simple working code that can be improved
- Support **exploration** - students should feel safe to modify and experiment
- Enable **understanding** - students must be able to explain what the code does

## Pedagogical Goals

Remember, the goal is NOT to write the most efficient or professional code. The goal is to:

1. ✅ Help students **learn Python fundamentals**
2. ✅ Build **confidence** through working code
3. ✅ Develop **problem-solving skills**
4. ✅ Foster **computational thinking**
5. ✅ Demonstrate **real-world development** with AI tools
6. ✅ Create **engaging, fun** learning experiences

## When to Break These Rules

You may use more advanced concepts when:

- Specifically requested by the teacher/instructor
- A student explicitly asks to learn a particular concept
- The educational benefit clearly outweighs the complexity
- You provide extra explanation and teaching comments

**Always prioritize learning over sophistication.**

## Example: Good vs. Not Appropriate

### ✅ GOOD - Simple and Clear

```python
def add_item_to_inventory(inventory, item):
    """Add an item to the player's inventory"""
    inventory.append(item)
    print(f"You picked up the {item}.")
```

### ❌ NOT APPROPRIATE - Too Advanced for Beginners

```python
def add_item(inventory: List[str], item: str) -> None:
    """Add an item to inventory with validation."""
    if not isinstance(item, str):
        raise TypeError("Item must be a string")
    inventory.append(item)
    print(f"You picked up the {item}.")
```

## Questions to Ask Yourself

Before suggesting code, consider:

1. Could a student who's been coding for 2 weeks understand this?
2. Does this follow patterns already established in the codebase?
3. Am I introducing new concepts unnecessarily?
4. Would I be able to explain every line to a complete beginner?
5. Does this code help the student learn, or just get the task done?

---

**Remember: You're not just writing code - you're teaching programming!**
