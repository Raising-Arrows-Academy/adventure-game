# 🎒 Add Inventory System

## Overview
Add a complete inventory system that allows players to pick up items, drop items, and view what they're carrying. This is a foundational feature that many other features will build upon.

## Difficulty
🟢 **Easy** - Great first feature to add!

## Prerequisites
- ✅ Base game is working (you can move between rooms and escape)
- ✅ You understand basic Python lists
- ✅ You've played the game at least once

## Python Concepts You'll Learn
- 📌 **Lists** - Storing multiple items in order
- 📌 **List methods** - `.append()`, `.remove()`, checking if item `in` list
- 📌 **String parsing** - Splitting commands like "take key" into parts
- 📌 **Conditionals** - Checking if items exist before taking/dropping
- 📌 **Dictionaries** - Adding items to room definitions

## 🎯 The Prompt

Copy this prompt and paste it into your AI assistant:

```
I'm working on a text adventure game in Python called Castle Escape. 
I'm a beginner learning Python basics.

I have a working game with:
- A dictionary called 'rooms' that stores room descriptions and exits
- A 'current_room' variable tracking player location
- A main game loop with a command parser
- Movement working (north, south, east, west)

I want to add an inventory system. Here's what I need:

REQUIREMENTS:
1. Create an empty list called 'inventory' to store items the player carries
2. Add items to rooms in the rooms dictionary (store as a list in each room)
3. Add 'take [item]' command - picks up item from current room, adds to inventory
4. Add 'drop [item]' command - removes item from inventory, adds to current room
5. Add 'inventory' or 'i' command - displays what player is carrying
6. Handle errors gracefully (trying to take item not in room, drop item not in inventory)

CODE STYLE:
- Use simple Python suitable for beginners (lists, dictionaries, functions, if/elif)
- NO classes or advanced features
- Add clear comments explaining what each section does
- Follow clean, readable code style
- Use helpful error messages for players

EXAMPLE ITEMS TO ADD:
- rusty key (in dungeon)
- torch (in hallway)
- sword (in courtyard)

Please provide:
1. The complete code changes needed
2. Brief explanation of how the inventory system works
3. Which parts of the existing code need to be modified

Make sure the code integrates smoothly with my existing game structure.
```

## 🧪 Testing Checklist

After adding the code, test these scenarios:

### Basic Functionality
- [ ] Type `inventory` or `i` - should show empty inventory at start
- [ ] Type `take key` in dungeon - should pick up the key
- [ ] Type `inventory` - should show the key in your inventory
- [ ] Type `drop key` - should drop the key in current room
- [ ] Type `inventory` - should show empty inventory again
- [ ] Type `look` - should see the key is now in the room

### Error Handling
- [ ] Try `take sword` in a room without a sword - should give helpful error
- [ ] Try `drop key` when you don't have a key - should give helpful error
- [ ] Try `take` with no item name - should ask what to take
- [ ] Try `take multiple words here` - should handle gracefully

### Game Flow
- [ ] Pick up multiple items - all should appear in inventory
- [ ] Move between rooms while carrying items - items should stay with you
- [ ] Drop items in different rooms - items should stay in those rooms
- [ ] Can still win the game with items in inventory

## 💭 Understanding the Code

After AI gives you the code, make sure you can answer these questions:

1. **Where is the inventory list created?** (Should be before the main game loop)
2. **How does the game know what items are in each room?** (Added to room dictionary)
3. **What does `.append()` do?** (Adds item to end of list)
4. **What does `.remove()` do?** (Removes item from list)
5. **Why do we check `if item in room['items']` before taking?** (To avoid errors)
6. **How does string parsing work for "take key"?** (Usually `command.split()` to separate words)

### Example Code Discussion Points

When reviewing the AI-generated code, look for:

- **List initialization:** `inventory = []`
- **Dictionary updates:** Adding `"items": ["rusty key"]` to room definitions
- **Conditional checks:** `if item in rooms[current_room]["items"]:`
- **List operations:** `inventory.append(item)`, `inventory.remove(item)`
- **Error messages:** Friendly messages when something can't be done

## 🎨 Extension Ideas

Once the basic inventory works, try these modifications:

### 🟢 Easy Extensions
- Add more items to discover
- Show inventory count: "You are carrying 3 items"
- Add item descriptions when you pick them up
- Make some items hidden (only appear after certain actions)

### 🟡 Medium Extensions
- Add weight limit (can only carry 5 items)
- Add item categories (keys, weapons, tools)
- Some items stack (3 torches), others don't (1 sword)
- Examine specific items: `examine sword` shows description

### 🔴 Advanced Extensions
- Items can be combined (key + sword = enchanted key)
- Items degrade with use (torch burns out)
- Item requirements for certain actions
- Container items (backpack holds more)

## 🐛 Common Issues and Solutions

### Issue: "KeyError: 'items'"
**Problem:** Some rooms don't have an 'items' key in the dictionary  
**Solution:** Make sure ALL rooms have `"items": []` even if the list is empty

### Issue: Items disappear when moving rooms
**Problem:** Items might be getting cleared somewhere  
**Solution:** Check that you're not reassigning the inventory list in the game loop

### Issue: Can take items that don't exist
**Problem:** Not checking if item exists before taking  
**Solution:** Use `if item in rooms[current_room]["items"]:` before taking

### Issue: "take" without item name crashes
**Problem:** Command parsing doesn't handle single-word commands  
**Solution:** Check length of command parts: `if len(parts) < 2:` show error

## 📚 Learning Reflections

After completing this feature, discuss:

1. **How do lists help organize data?**
   - What's the difference between a list and a variable?
   - When would you use a list vs. other data structures?

2. **How does error handling improve user experience?**
   - What happens without error checks?
   - How do good error messages help players?

3. **How does this feature connect to others?**
   - What other features might need an inventory?
   - How might you extend this system?

## 🎯 Next Steps

Once your inventory system works perfectly:

1. ✅ Try `01_adding_features/add_locked_door.md` - Uses inventory for keys!
2. ✅ Try `02_expanding_world/add_items.md` - Add more interesting items
3. ✅ Try `01_adding_features/add_combat_system.md` - Weapons from inventory

## 🎓 Teacher Notes

**Class Time:** 30-45 minutes (including testing)

**Learning Objectives:**
- Understand Python lists and list methods
- Practice reading and modifying existing code
- Learn proper error handling
- Experience iterative testing

**Discussion Questions:**
- "Why did the AI structure the code this way?"
- "What would happen if we didn't check for errors?"
- "How would you add a weight limit?"
- "What other games use inventory systems?"

**Common Student Mistakes:**
- Forgetting to add items to ALL rooms (even empty lists)
- Not testing edge cases
- Copying code without reading it
- Skipping error handling

---

**Great choice for your first feature!** The inventory system is fundamental and you'll use it in many other features. Take your time to understand how it works! 🎒✨
