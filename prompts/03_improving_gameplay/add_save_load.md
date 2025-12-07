# 💾 Add Save and Load System

## Overview
Add the ability to save game progress and load it later! This lets players take breaks and return to their adventure, save before risky decisions, or preserve high scores.

## Difficulty
🟡 **Medium** - Introduces file I/O (reading and writing files)

## Prerequisites
- ✅ Base game is working
- ✅ You have features worth saving (inventory, unlocked doors, score, etc.)
- ✅ You understand how variables store game state
- ✅ Ready to learn a new concept (file I/O)

## Python Concepts You'll Learn
- 📌 **File I/O** - Reading from and writing to files
- 📌 **JSON format** - Storing data in a structured way
- 📌 **import json** - Using Python's JSON module
- 📌 **State management** - Tracking what needs to be saved
- 📌 **Error handling** - Dealing with missing save files

## 🎯 The Prompt

Copy this prompt and paste it into your AI assistant:

```
I'm working on Castle Escape, a Python text adventure game for beginners.

I have working:
- Room navigation (current_room variable)
- Inventory system (inventory list)
- [LIST OTHER STATE: score, unlocked doors, defeated enemies, etc.]

I want to add save and load functionality so players can save their progress and 
continue later.

REQUIREMENTS:

SAVE FUNCTIONALITY:
1. Add 'save' command
2. Save to a file called "castle_save.json"
3. Save current game state:
   - Current room
   - Inventory (list of items)
   - Score (if exists)
   - Door lock states (if exists)
   - Enemy defeated flags (if exists)
   - [ANY OTHER STATE VARIABLES]
4. Confirm when save is successful
5. Use JSON format for easy reading/writing

LOAD FUNCTIONALITY:
1. Add 'load' command  
2. Read from "castle_save.json"
3. Restore all saved game state
4. Handle case where no save file exists (helpful error)
5. Confirm when load is successful
6. Show current status after loading

AUTO-SAVE (optional):
- Save automatically when quitting
- Ask if player wants to save

CODE STYLE:
- Use simple Python with JSON module
- Import json at top: `import json`
- Add clear comments
- Use helpful error messages
- Include try/except for file errors

Please provide:
1. Import statement needed
2. Save function code
3. Load function code
4. Integration with main game loop
5. Example of what the save file will look like

Explain how JSON works in simple terms for a beginner.
```

## 🧪 Testing Checklist

After adding save/load:

### Save Testing
- [ ] Type `save` - should create castle_save.json file
- [ ] Get confirmation message
- [ ] File exists in same directory as your game
- [ ] Can open and read the save file (it's human-readable JSON)
- [ ] Save file contains all important game state

### Load Testing
- [ ] Make changes to game state (move, pick up items, earn points)
- [ ] Type `save`
- [ ] Quit the game
- [ ] Start game again
- [ ] Type `load`
- [ ] Verify you're in the same room
- [ ] Verify inventory is the same
- [ ] Verify all state is restored correctly

### Error Handling
- [ ] Try `load` when no save file exists - should show helpful message
- [ ] Delete a line from save file, try to load - should handle gracefully
- [ ] Save multiple times - should overwrite old save

### Edge Cases
- [ ] Save with empty inventory - should load empty
- [ ] Save and load immediately (no changes) - should work
- [ ] Play through whole game after loading - should work normally

## 💭 Understanding the Code

After AI gives you the code, make sure you can answer:

1. **What is JSON?** (JavaScript Object Notation - a text format for storing data)
2. **What does `import json` do?** (Gives us tools to work with JSON files)
3. **How do we write to a file?** (`with open("file.json", "w") as f:`)
4. **How do we read from a file?** (`with open("file.json", "r") as f:`)
5. **What is `json.dump()`?** (Writes Python data to JSON file)
6. **What is `json.load()`?** (Reads JSON file into Python data)
7. **What is try/except?** (Handles errors gracefully)
8. **Where is game state stored?** (In variables like current_room, inventory, score)

### Example Code Discussion Points

Look for these patterns:

```python
import json  # At top of file

# Save function
def save_game(current_room, inventory, score):
    game_state = {
        "current_room": current_room,
        "inventory": inventory,
        "score": score
    }
    with open("castle_save.json", "w") as save_file:
        json.dump(game_state, save_file)
    print("Game saved!")

# Load function
def load_game():
    try:
        with open("castle_save.json", "r") as save_file:
            game_state = json.load(save_file)
        return game_state
    except FileNotFoundError:
        print("No save file found!")
        return None
```

### What a Save File Looks Like

```json
{
    "current_room": "hallway",
    "inventory": ["rusty key", "torch", "sword"],
    "score": 45,
    "door_locked": false,
    "guard_defeated": true
}
```

It's readable by humans AND computers!

## 🎨 Extension Ideas

Once basic save/load works:

### 🟢 Easy Extensions
- **Multiple save slots:**
  - save1.json, save2.json, save3.json
  - Command: `save 1`, `load 1`

- **Save file info:**
  - Add timestamp to save
  - Add game version
  - Add player name

- **Auto-save:**
  - Save automatically every N moves
  - Save when quitting
  - Save before risky actions

### 🟡 Medium Extensions
- **Save menu:**
  - List all save files
  - Show when each was created
  - Delete old saves

- **Quick save:**
  - Dedicated key for instant save
  - Separate quicksave file

- **Checkpoint system:**
  - Auto-save at key points
  - Can only load from checkpoints

- **Cloud saves:**
  - Save to a server (advanced!)
  - Share saves between computers

### 🔴 Advanced Extensions
- **Save compression:**
  - Smaller file size
  - Encrypted saves (prevent cheating)

- **Save states:**
  - Like emulator save states
  - Can save/load any moment

- **Replay system:**
  - Save all commands entered
  - Can replay playthrough

## 🐛 Common Issues and Solutions

### Issue: "ModuleNotFoundError: No module named 'json'"
**Problem:** Python version too old (unlikely) or typo  
**Solution:** JSON is built-in to Python 3, check your spelling

### Issue: Save file is empty or corrupted
**Problem:** Not using `with` statement or error during save  
**Solution:** Use `with open()` - it handles closing the file properly

### Issue: Variables don't restore after load
**Problem:** Not assigning loaded values back to variables  
**Solution:** 
```python
current_room = game_state["current_room"]
inventory = game_state["inventory"]
```

### Issue: "FileNotFoundError" when loading
**Problem:** No save file exists yet  
**Solution:** Use try/except to handle gracefully:
```python
try:
    # load code
except FileNotFoundError:
    print("No save file found. Start a new game!")
```

### Issue: Can't find save file after saving
**Problem:** Saved to different directory  
**Solution:** Save file is in same directory as your .py file. Use full path if needed.

### Issue: Boolean values won't save
**Problem:** JSON uses lowercase `true/false`, Python uses `True/False`  
**Solution:** JSON handles this automatically, but load them correctly:
```python
door_locked = game_state["door_locked"]  # Works fine
```

## 📚 Learning Reflections

After adding save/load, discuss:

1. **File I/O Concepts**
   - What's the difference between reading and writing?
   - Why use `with` statement?
   - What is a file path?

2. **Data Formats**
   - Why use JSON instead of plain text?
   - How is JSON similar to Python dictionaries?
   - What other data formats exist?

3. **State Management**
   - What is "game state"?
   - Which variables need to be saved?
   - What happens if we forget to save something?

4. **Error Handling**
   - Why handle errors instead of crashing?
   - What errors might occur with files?
   - How do we give users helpful feedback?

## 🔒 Important Notes

### File Safety
- Save files are NOT encrypted - players can edit them
- For a learning project, this is fine (and interesting!)
- In real games, you'd want protection against cheating

### Version Compatibility
- If you update your game, old saves might break
- Good practice: include version number in save file
- Check version when loading, warn if mismatch

### User Experience
- Always confirm when save succeeds
- Warn before overwriting
- Make it hard to accidentally lose progress

## 🎯 Next Steps

Once save/load works:

1. ✅ Add multiple save slots
2. ✅ Try `03_improving_gameplay/add_scoring_system.md` - Save high scores
3. ✅ Add timestamps to saves
4. ✅ Create "new game / continue" menu on startup

## 🎓 Teacher Notes

**Class Time:** 45-60 minutes

**Learning Objectives:**
- Understand file input/output
- Learn JSON data format
- Practice error handling
- Think about program state

**Discussion Questions:**
- "Why would a game need save files?"
- "What could go wrong with file operations?"
- "How would you prevent save file cheating?"
- "What other programs use save files?"

**Common Student Mistakes:**
- Forgetting to import json
- Not using `with` statement (file doesn't close)
- Not assigning loaded values back to variables
- Saving strings instead of actual variables
- No error handling for missing file
- Overwriting file accidentally

**Demo Activity:**
1. Show save file in text editor
2. Edit it manually (change score)
3. Load and show it worked
4. Discuss implications (cheating, corrupted files)

**Extension Discussion:**
- How do online games save? (servers)
- What's the difference between save files and databases?
- How do games detect save file tampering?

**Cross-Curricular:**
- **Computer Science:** File systems, data persistence
- **Ethics:** Is editing save files cheating?
- **Career:** How do real games handle saves?

---

**Save files are essential!** They let players take breaks and preserve their achievements. Understanding file I/O is an important programming skill you'll use in many projects. 💾✨
