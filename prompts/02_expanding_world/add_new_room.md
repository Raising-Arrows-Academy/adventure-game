# 🏰 Add New Room to Your Castle

## Overview
Expand your castle by adding new rooms! This template helps you plan and add rooms to make your adventure bigger and more interesting.

## Difficulty
🟢 **Easy** - Great way to customize your game!

## Prerequisites
- ✅ Base game is working
- ✅ You understand the room dictionary structure
- ✅ You've played through the current rooms

## Python Concepts You'll Learn
- 📌 **Dictionary expansion** - Adding new entries to existing dictionary
- 📌 **Two-way connections** - Making sure paths work both directions
- 📌 **Game world design** - Planning logical room layouts

## 🎯 Planning Your Room

Before you use the prompt, answer these questions:

### Room Details
- **Room Name:** _________________ (one word, lowercase, e.g., "library")
- **Description:** What does the player see when they enter?
  
  _________________________________________________________________________
  
  _________________________________________________________________________

- **Connected to:** Which existing room(s) will connect to this one?
  
  _________________________________________________________________________

- **Which direction(s):** How do you reach the new room?
  
  From _____________ go _____________ to reach _____________

- **Items in room:** What can players find here? (optional)
  
  _________________________________________________________________________

### Room Ideas

Need inspiration? Try these:

**Classic Castle Rooms:**
- 🏛️ **Throne Room** - Grand hall with a throne, tapestries, suits of armor
- 📚 **Library** - Books, scrolls, maybe a secret passage
- 🍳 **Kitchen** - Cooking supplies, food, knives, pots and pans
- 🛏️ **Bedroom** - Royal chambers, bed, wardrobe, treasures
- 🗼 **Tower** - High up with a window view, maybe locked door to roof
- ⚗️ **Alchemy Lab** - Potions, ingredients, mysterious equipment
- 🏺 **Treasury** - Gold, jewels, valuable items, probably guarded
- ⛪ **Chapel** - Peaceful room, maybe healing items or sanctuary
- 🏃 **Armory** - Weapons, shields, armor to collect
- 🌊 **Dungeon (lower level)** - More cells, prisoners, secrets

**Outdoor/Special Areas:**
- 🌲 **Garden** - Plants, fountain, peaceful or overgrown
- 🏇 **Stables** - Horses, hay, tack, possible escape route
- 🌉 **Drawbridge** - Crossing the moat, entrance control
- 🗿 **Secret Passage** - Hidden route between rooms

## 🎯 The Prompt Template

Copy this template and fill in YOUR room details:

```
I'm working on Castle Escape, a Python text adventure game.

My current game has rooms in a dictionary where each room has:
- "description": text describing the room  
- Direction keys ("north", "south", "east", "west"): which rooms they lead to
- "items": list of items in the room (if inventory system is added)

I want to add a new room to my castle.

NEW ROOM DETAILS:
- Room name: [YOUR ROOM NAME]
- Description: "[YOUR DESCRIPTION - make it vivid and interesting!]"
- Connected to: [EXISTING ROOM NAME] to the [DIRECTION], player goes [OPPOSITE DIRECTION] to return
- Items in room: [LIST ITEMS or say "none"]

REQUIREMENTS:
1. Add the new room to the rooms dictionary
2. Update BOTH rooms' connections (two-way path)
   - Add exit from [EXISTING ROOM] going [DIRECTION] to new room
   - Add exit from new room going [OPPOSITE DIRECTION] back
3. Include items list (empty list [] if no items)
4. Make sure description is engaging and descriptive

CODE STYLE:
- Match the existing rooms dictionary format exactly
- Use simple, clear Python
- Add comments showing what was added

Please show me:
1. The new room entry in the dictionary
2. The updated connections in the existing room
3. A reminder to test the connections work both ways

Example format to follow:
"library": {
    "description": "You are in a dusty library. Bookshelves tower to the ceiling.\nThere is a door to the SOUTH.",
    "south": "hallway",
    "items": ["old book", "candle"]
}
```

### Example Filled-In Prompt

Here's how a completed prompt might look:

```
I'm working on Castle Escape, a Python text adventure game.

My current game has a rooms dictionary with dungeon, hallway, and courtyard.

I want to add a new room to my castle.

NEW ROOM DETAILS:
- Room name: library
- Description: "You enter a magnificent library. Dusty bookshelves reach to the vaulted ceiling, and a large oak desk sits in the center. Moonlight streams through a stained glass window. There are doors to the SOUTH and EAST."
- Connected to: hallway to the EAST (player goes WEST to return to hallway)
- Also connected to: tower to the NORTH from the library
- Items in room: ["ancient book", "candle", "reading glasses"]

REQUIREMENTS:
1. Add the library to the rooms dictionary
2. Update hallway: add "east": "library"
3. Update library: add "west": "hallway"
4. Include items list

Please show the complete new room entry and the update to the hallway room.
```

## 🧪 Testing Checklist

After adding your new room:

### Navigation Tests
- [ ] From the connected room, type the direction to your new room - should work
- [ ] From your new room, type the opposite direction - should go back
- [ ] Type `look` in new room - description should display correctly
- [ ] Try invalid directions from new room - should give appropriate error

### Integration Tests
- [ ] Make sure all old rooms still work correctly
- [ ] Can still complete the game (reach freedom)
- [ ] Items (if any) can be picked up from new room
- [ ] Moving through new room doesn't break game flow

### Description Quality
- [ ] Description is clear and interesting
- [ ] Exits are mentioned in the description
- [ ] Room fits the theme of a castle
- [ ] No typos or grammar errors

## 💭 Understanding the Code

After adding your room, make sure you understand:

1. **Dictionary structure:**
   ```python
   "room_name": {
       "description": "text here",
       "north": "other_room",
       "items": []
   }
   ```

2. **Two-way connections:** If room A can go north to room B, then room B must be able to go south back to room A

3. **Item lists:** Even rooms with no items need `"items": []` if inventory system exists

## 🎨 Extension Ideas

Once you've added one room successfully:

### 🟢 Easy Extensions
- Add 2-3 more connected rooms
- Create a full floor of the castle
- Add special descriptions for first time entering vs. returning
- Place items strategically (key in one room, locked door using it in another)

### 🟡 Medium Extensions
- Create multiple floors (upstairs, downstairs)
- Add secret passages (hidden connections)
- Rooms that change based on events (before/after defeating boss)
- One-way passages (slide down, can't go back)

### 🔴 Advanced Extensions
- Random room generation
- Room states that change over time
- Puzzles that unlock new rooms
- Expandable castle that grows as player progresses

## 🐛 Common Issues and Solutions

### Issue: Can go TO new room but not BACK
**Problem:** Forgot to update one direction  
**Solution:** Make sure BOTH rooms have the connection:
- Room A: `"north": "room_b"`
- Room B: `"south": "room_a"`

### Issue: "KeyError" when entering room
**Problem:** Typo in room name or connection  
**Solution:** Check exact spelling matches in both places

### Issue: Description doesn't match available exits
**Problem:** Description says "north" but no north exit exists  
**Solution:** Make sure description text matches actual dictionary keys

### Issue: Can't find new room
**Problem:** Might have connected it to wrong room  
**Solution:** Draw a map on paper showing connections

### Issue: Comma or syntax errors
**Problem:** Missing comma between rooms in dictionary  
**Solution:** Check for comma after the closing `}` of each room (except the last one)

## 🗺️ Map Your Castle

Draw your castle layout! This helps plan room connections:

```
         Tower
           |
    Library-Hallway-Courtyard-Freedom
           |
        Dungeon
```

Use arrows to show which directions connect rooms:
- North = ↑
- South = ↓  
- East = →
- West = ←

## 📚 Learning Reflections

After adding your room, discuss:

1. **World Design**
   - How do room connections affect gameplay?
   - What makes a room interesting to explore?
   - How does room layout create challenge?

2. **Data Structure**
   - Why use a dictionary for rooms?
   - How do nested dictionaries work?
   - What are the benefits of this structure?

3. **Creative Decisions**
   - Why did you choose this room?
   - How does it fit the story?
   - What items make sense here?

## 🎯 Next Steps

Once you've successfully added a room:

1. ✅ Add 2-3 more rooms to create a complete area
2. ✅ Try `02_expanding_world/add_items.md` - Add interesting items to your new rooms
3. ✅ Try `01_adding_features/add_locked_door.md` - Lock some connections
4. ✅ Plan a complete castle with multiple areas

## 🎓 Teacher Notes

**Class Time:** 15-20 minutes per room

**Learning Objectives:**
- Understand dictionary structure and nesting
- Practice careful syntax (commas, quotes, colons)
- Think about spatial relationships
- Design coherent game worlds

**Discussion Questions:**
- "How does room layout affect gameplay?"
- "What makes a good room description?"
- "How would you plan a 10-room castle?"
- "What's the difference between linear and branching layouts?"

**Common Student Mistakes:**
- Forgetting return path (one-way only)
- Typos in room names
- Missing commas in dictionary
- Description doesn't match available exits
- Rooms that don't fit the theme

**Group Activity:**
- Have students design a complete castle floor together
- Each student adds one room
- Must connect logically
- Create a class castle map

**Extension Activity:**
Students can create themed wings:
- Student 1: Royal quarters (bedroom, throne room, balcony)
- Student 2: Service areas (kitchen, servant quarters, storage)
- Student 3: Defense (armory, barracks, tower)
- Then connect them all together!

---

**Build your dream castle!** Every great adventure needs interesting places to explore. Think about what makes each room unique and how they connect to tell a story. 🏰✨
