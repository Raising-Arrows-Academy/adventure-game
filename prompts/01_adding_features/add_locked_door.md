# 🔑 Add Locked Door Mechanic

## Overview
Add locked doors that require specific keys to open. This creates puzzles where players must find keys before they can progress, making the game more challenging and interesting.

## Difficulty
🟢 **Easy** - Builds directly on inventory system

## Prerequisites
- ✅ Inventory system is working (can pick up and carry items)
- ✅ You understand how boolean variables work (True/False)
- ✅ You understand if/elif statements with multiple conditions

## Python Concepts You'll Learn
- 📌 **Boolean state tracking** - Using True/False variables
- 📌 **Multiple conditions** - Checking both room AND key possession
- 📌 **State changes** - Unlocking doors permanently
- 📌 **Conditional navigation** - Blocking movement until conditions met

## 🎯 The Prompt

Copy this prompt and paste it into your AI assistant:

```
I'm working on Castle Escape, a Python text adventure game for beginners.

I have working:
- Room navigation system (movement between rooms)
- Inventory system (can pick up, drop, and carry items)
- A 'rusty key' item in the dungeon

I want to add a locked door mechanic. Here's what I need:

REQUIREMENTS:
1. Add a locked door between the hallway and courtyard
2. Door starts locked (boolean variable or flag)
3. When player tries to go north from hallway, check:
   - If door is unlocked, let them through
   - If door is locked AND player has 'rusty key', unlock it and let them through
   - If door is locked AND player lacks key, show "locked door" message
4. Once unlocked, door stays unlocked for the rest of the game
5. Show clear messages for each scenario

CODE STYLE:
- Use simple Python (boolean variables, if/elif/else, checking lists)
- NO classes or complex structures
- Add clear comments
- Provide helpful messages to guide the player

Please provide:
1. How to track if the door is locked (boolean variable)
2. Modified movement code to check door status
3. Messages for each scenario (locked, unlocking, already unlocked)
4. Where to add this code in my existing game

The code should integrate smoothly without breaking existing functionality.
```

## 🧪 Testing Checklist

After adding the code, test these scenarios:

### Without the Key
- [ ] Start a new game (door should be locked)
- [ ] Go north to hallway
- [ ] Try to go north to courtyard - should show "door is locked" message
- [ ] Try going south back to dungeon - should work normally
- [ ] Try going north again - still locked

### With the Key
- [ ] Start a new game
- [ ] In dungeon, type `take key`
- [ ] Go north to hallway
- [ ] Go north toward courtyard - should unlock and let you through
- [ ] Check that you can now move back and forth freely (door stays unlocked)

### Edge Cases
- [ ] Drop the key after unlocking - should still be able to go through
- [ ] Try using the key on other directions - should not affect them
- [ ] Make sure you can still win the game

## 💭 Understanding the Code

After AI gives you the code, make sure you can answer these questions:

1. **Where is the door's locked status stored?** (Boolean variable like `door_locked = True`)
2. **When does the game check if door is locked?** (When player tries to move north from hallway)
3. **How do we check if player has the key?** (`if "rusty key" in inventory:`)
4. **What happens when door is unlocked?** (`door_locked = False`)
5. **Why does the door stay unlocked?** (Boolean variable persists through game loop)
6. **What's the order of checks?** (Check direction → check if locked → check if has key)

### Example Code Discussion Points

Look for these patterns in the AI-generated code:

```python
# Boolean variable to track door state
door_locked = True

# In movement code, check conditions
if command == "north" and current_room == "hallway":
    if door_locked:
        if "rusty key" in inventory:
            door_locked = False  # Unlock permanently
            print("You use the rusty key to unlock the door!")
            current_room = "courtyard"
        else:
            print("The door is locked. You need a key!")
    else:
        print("The door is already unlocked.")
        current_room = "courtyard"
```

## 🎨 Extension Ideas

Once the basic locked door works, try these modifications:

### 🟢 Easy Extensions
- Add more locked doors in other locations
- Different keys for different doors (golden key, silver key)
- Add a message when you pick up the key hinting at its use
- Show different messages for first unlock vs. already unlocked

### 🟡 Medium Extensions
- Doors that can be re-locked with a command
- Doors that need multiple items (key AND password)
- Keys that break after one use
- Hidden doors that only appear after certain actions
- One-way doors (can go through one direction only)

### 🔴 Advanced Extensions
- Lockpicking mechanic (try without key, random success chance)
- Combination locks (enter 3-digit code)
- Keys found by solving puzzles
- Doors that unlock automatically after certain events
- Master key that opens multiple doors

## 🐛 Common Issues and Solutions

### Issue: Door unlocks from any room
**Problem:** Not checking current_room before unlocking  
**Solution:** Add `and current_room == "hallway"` to the condition

### Issue: Door stays locked even with key
**Problem:** Condition might be checking wrong variable or using wrong item name  
**Solution:** Print the inventory to debug: `print(inventory)` and check item names match exactly

### Issue: Error when trying to go north
**Problem:** Might have broken the normal movement code  
**Solution:** Make sure the locked door check is ONLY for the specific room/direction combo

### Issue: Can use key from any room
**Problem:** Not requiring player to be at the door  
**Solution:** Only check for key when player is in the hallway going north

### Issue: Door works once then breaks
**Problem:** Might be resetting door_locked variable in the loop  
**Solution:** Initialize `door_locked = True` BEFORE the game loop, not inside it

## 📚 Learning Reflections

After completing this feature, discuss:

1. **How do boolean variables help track state?**
   - What's the difference between True/False and "yes"/"no" strings?
   - Why use booleans for game states?

2. **Why check multiple conditions?**
   - What happens if we only check for the key, not the room?
   - How does order of conditions matter?

3. **How does this create gameplay?**
   - How do locked doors make the game more interesting?
   - What other real-world objects work like this?

4. **State management**
   - Why does the door stay unlocked?
   - What would happen if we reset door_locked each loop?

## 🎯 Next Steps

Once your locked door works perfectly:

1. ✅ Add more rooms and locked doors throughout the castle
2. ✅ Try `02_expanding_world/add_items.md` - Add more keys and items
3. ✅ Try `01_adding_features/add_combat_system.md` - Add guards protecting keys
4. ✅ Create custom puzzle: door needs multiple items to unlock

## 🎓 Teacher Notes

**Class Time:** 20-30 minutes

**Learning Objectives:**
- Understand boolean state tracking
- Practice compound conditional statements
- Learn about game state management
- Experience debugging multiple conditions

**Discussion Questions:**
- "What other game mechanics use True/False states?"
- "How would you add a second locked door with a different key?"
- "What's the difference between permanent and temporary state changes?"
- "How could we make the key reusable vs. single-use?"

**Common Student Mistakes:**
- Initializing boolean inside the game loop (resets each iteration)
- Not checking current_room (unlocks from anywhere)
- Wrong item name in condition (case sensitivity)
- Breaking existing movement code
- Forgetting to set door_locked = False when unlocking

**Extension Activity:**
Have students design a "three key door" that needs three different keys to unlock. This practices:
- Multiple boolean variables OR
- Counting items in inventory OR  
- Checking for multiple items in a list

**Cross-curricular Connection:**
- Physics: Keys and locks as simple machines
- History: Medieval castle security
- Logic: Boolean algebra basics

---

**Locked doors create puzzles!** This simple mechanic can make your game much more interesting. Think about where else you could use state tracking (turned on/off, completed/incomplete, etc.). 🔑✨
