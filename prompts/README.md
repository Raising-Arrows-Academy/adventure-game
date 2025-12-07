# 🎯 AI Prompt Library for Castle Escape

Welcome to the **AI Prompt Library**! This collection of ready-to-use prompts will help you learn how to effectively use AI to develop features for the Castle Escape text adventure game.

## 📚 What Are Prompts?

A **prompt** is a clear, specific instruction you give to an AI assistant (like ChatGPT, GitHub Copilot, or Claude) to help you accomplish a task. Think of it like giving directions to a very smart friend who's helping you code!

**Good prompts** = Better AI responses = Faster learning

## 🎓 Why This Library Exists

This library teaches you **two things at once**:

1. **Python Programming** - You'll build real features and learn how they work
2. **Prompt Engineering** - You'll learn how to communicate effectively with AI tools

## 📂 Directory Guide

### 🟢 Easy - Start Here!

**01_adding_features/** - Add core game mechanics
- `add_inventory_system.md` - Pick up, drop, and view items ⭐ **Start here!**
- `add_locked_door.md` - Doors that need keys to open
- `add_combat_system.md` - Fight enemies with health and attacks

**04_polish/** - Make your game look and feel better
- `improve_descriptions.md` - More engaging room text
- `add_ascii_art.md` - Text-based graphics for flair

### 🟡 Medium - Build On What You Know

**02_expanding_world/** - Make your castle bigger
- `add_new_room.md` - Add more places to explore
- `add_items.md` - Create interesting objects

**03_improving_gameplay/** - Advanced features
- `add_scoring_system.md` - Track points and achievements
- `add_save_load.md` - Save and load game progress

### 🔴 When Things Go Wrong

**05_debugging/** - Fix problems in your code
- `debug_error.md` - Handle error messages
- `fix_logic_bug.md` - Fix code that runs but does the wrong thing

### 📝 Templates - Create Your Own

**templates/** - Build custom prompts
- `feature_template.md` - Template for new feature ideas
- `custom_prompt_worksheet.md` - Planning worksheet for custom features

## 🚀 How to Use This Library

### For Your First Feature (Recommended Path)

1. **Make sure the base game works**
   ```bash
   python main.py
   ```
   Select Castle Escape and try playing. You should be able to move around and escape.

2. **Start with the Inventory System** 🎒
   - Open `01_adding_features/add_inventory_system.md`
   - Copy the prompt from that file
   - Paste it into your AI assistant (ChatGPT, Copilot, Claude, etc.)
   - Read and understand the code AI generates
   - Add it to your game file (`castle_escape/castle_escape.py`)
   - Test it thoroughly!

3. **Move on to Locked Doors** 🔑
   - Open `01_adding_features/add_locked_door.md`
   - Follow the same process
   - Notice how this builds on the inventory system

4. **Keep building!** 🏗️
   - Try other features in order of difficulty
   - Mix and match based on what interests you
   - Create your own custom features using the templates

### For Each Prompt You Use

✅ **Before using the prompt:**
- Read the prerequisites - do you have what you need?
- Understand what the feature will do
- Check the difficulty level - is it right for you now?

✅ **When using the prompt:**
- Copy it exactly as written (or customize using the instructions)
- Paste it into your AI assistant
- Read the AI's response carefully before copying code

✅ **After getting the code:**
- **READ the code** - don't just copy it blindly!
- Ask AI to explain any parts you don't understand
- Add the code to your game file
- **TEST thoroughly** using the testing checklist
- Try breaking it - what happens with weird inputs?

✅ **Understanding the code:**
- Can you explain what each part does?
- What Python concepts are being used?
- How does it connect to code you already have?
- Could you modify it to work differently?

## 💡 Tips for Writing Effective Prompts

### ✅ DO:
- **Be specific** - "Add an inventory system that lets players pick up, drop, and view items" is better than "add items"
- **Give context** - Tell AI what you already have working
- **Ask for explanations** - "Explain how this code works" or "Add comments to explain each part"
- **Request beginner-friendly code** - "Use simple Python - I'm a beginner"
- **Include your constraints** - "Don't use classes, I haven't learned those yet"

### ❌ DON'T:
- **Be vague** - "Make the game better" doesn't give AI enough direction
- **Forget prerequisites** - Don't ask for combat before you have health tracking
- **Skip testing** - Always test AI-generated code!
- **Copy blindly** - Always read and understand the code first
- **Ignore errors** - If something doesn't work, use the debugging prompts

## 📊 Prompt Quality Levels

### Basic Prompt (Works, but could be better)
```
Add an inventory to the game
```

### Good Prompt (Specific and clear)
```
Add an inventory system to castle_escape.py that:
- Stores items in a Python list
- Allows 'take [item]' command to pick up items
- Allows 'drop [item]' command to drop items
- Allows 'inventory' command to see what you're carrying
Use beginner-friendly Python code with comments explaining what each part does.
```

### Excellent Prompt (Context + specifics + learning goals)
```
I'm building a text adventure game in Python (castle_escape.py). I'm a beginner 
and have a working game with room navigation using dictionaries and a while loop.

I want to add an inventory system. Here's what I need:

FUNCTIONALITY:
- Store items the player is carrying in a list called 'inventory'
- Add 'take [item]' command to pick up items from rooms
- Add 'drop [item]' command to drop items in current room
- Add 'inventory' or 'i' command to view carried items
- Items in rooms should be stored in the room dictionary
- When you take an item, remove it from the room and add to inventory
- When you drop an item, remove from inventory and add to room

CODE REQUIREMENTS:
- Use simple Python - lists, dictionaries, functions, if/elif
- No classes or advanced features
- Add clear comments explaining each section
- Follow the existing code style in my game

Please provide the code and explain how it works.
```

## 🎯 Learning Paths by Session

### Session 1-2: Getting Started
- Read this README
- Add inventory system
- Test and understand how it works
- Discussion: How do lists work in Python?

### Session 3-4: Building on Basics
- Add locked door mechanic
- Add 2-3 new rooms
- Add items to rooms
- Discussion: How do dictionaries and boolean states work together?

### Session 5-6: Combat and Challenge
- Add combat system
- Add multiple enemies
- Add scoring
- Discussion: How does random number generation work?

### Session 7-8: Polish and Expansion
- Improve descriptions
- Add ASCII art
- Add save/load feature
- Discussion: How does file I/O work?

### Session 9-10: Your Own Ideas
- Use templates to create custom features
- Debug any issues
- Share with classmates
- Discussion: What makes a good prompt? What did you learn?

## 🔧 Troubleshooting

### "The AI gave me code that doesn't work"
1. Check the error message - what does it say?
2. Use `05_debugging/debug_error.md` to get help
3. Make sure you copied all the code
4. Check that you have the prerequisites working

### "I don't understand the code AI generated"
1. Ask AI to explain it: "Can you explain this code line by line?"
2. Ask AI to add more comments: "Add detailed comments explaining what each part does"
3. Ask your teacher or a classmate
4. Try changing small things and see what happens (great way to learn!)

### "The code works but does the wrong thing"
1. Use `05_debugging/fix_logic_bug.md` to describe the problem
2. Explain what you expected vs. what actually happens
3. AI can help you fix logic errors

### "I want to add something not in this library"
1. Use `templates/custom_prompt_worksheet.md` to plan your feature
2. Use `templates/feature_template.md` to structure your prompt
3. Share your custom prompt with the class!

## 🎓 For Teachers

### Classroom Integration

**Individual Work:**
- Students choose features to implement
- Use prompts to learn at their own pace
- Build unique versions of the game

**Pair Programming:**
- Partners work together using prompts
- One person prompts AI, other reviews code
- Switch roles for each feature

**Whole Class:**
- Demonstrate using prompts together
- Discuss the AI-generated code as a group
- Compare different approaches AI suggested

**Assessment Opportunities:**
- Can students explain AI-generated code?
- Can they modify code to add variations?
- Can they write their own effective prompts?
- Can they debug AI-generated code?

### Discussion Questions
- "What made this prompt work well?"
- "How is working with AI different from coding alone?"
- "What did AI get wrong? How did you fix it?"
- "What Python concept did this feature teach you?"
- "How would you modify this feature to be different?"

## 🌟 Contributing Your Own Prompts

Did you create a great custom feature? Share it!

1. Use the feature template to document your prompt
2. Test it with AI to make sure it works
3. Share with your teacher to add to the library
4. Help other students learn from your creativity!

## 📖 Additional Resources

**Python Help:**
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python](https://www.w3schools.com/python/)

**AI & Prompt Engineering:**
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [GitHub Copilot Documentation](https://docs.github.com/copilot)

**Text Adventure Games:**
- [Interactive Fiction Archive](https://www.ifarchive.org/)
- Examples of what text games can become!

---

## 🎮 Ready to Start?

1. ✅ Make sure the base game works
2. ✅ Open `01_adding_features/add_inventory_system.md`
3. ✅ Follow the instructions
4. ✅ Start building your adventure!

**Remember:** AI is a tool to help you learn, not replace learning. Always read, understand, and test the code. Ask questions. Make mistakes. Have fun! 🚀

---

*Happy coding! May your prompts be clear and your adventures epic!* 🏰✨
