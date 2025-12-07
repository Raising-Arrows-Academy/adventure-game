# 💎 Add Items to Your Game

## Overview
Add interesting items that players can interact with! Items can be simple collectibles, useful tools, quest objects, or puzzle pieces that make your game more engaging.

## Difficulty
🟢 **Easy** - Simple if inventory system exists, creates lots of possibilities

## Prerequisites
- ✅ Inventory system is working (can pick up and carry items)
- ✅ You understand how lists work
- ✅ You have rooms to place items in

## Python Concepts You'll Learn
- 📌 **Dictionary properties** - Items can have attributes (description, usable, etc.)
- 📌 **List management** - Adding items to room item lists
- 📌 **Conditional logic** - Special item behaviors
- 📌 **Game design** - Creating meaningful items

## 🎯 Planning Your Items

Before using the prompt, think about your items:

### Item Types

**Collectibles** (just for inventory/scoring)
- Coins, gems, treasures
- Quest items to deliver
- Set pieces (collect all 5 crystals)

**Tools** (enable actions)
- Keys (unlock doors)
- Weapons (for combat)
- Torches (light dark rooms)
- Rope (climb down walls)

**Consumables** (used once)
- Healing potions
- Food
- Magic scrolls

**Puzzle Items** (combine or use in specific ways)
- Pieces that fit together
- Clues (notes, maps)
- Ingredients for recipes

### Item Properties to Consider

- **Name:** What's it called?
- **Location:** Which room is it in?
- **Description:** What does it look like?
- **Function:** What does it do? (if anything)
- **Usable:** Can it be "used" or just carried?

## 🎯 The Prompt Template

### For Simple Items (Just Collectible)

```
I'm working on Castle Escape, a Python text adventure game with an inventory system.

I want to add collectible items to various rooms.

ITEMS TO ADD:
1. [ITEM NAME] in [ROOM NAME] - [brief description]
2. [ITEM NAME] in [ROOM NAME] - [brief description]  
3. [ITEM NAME] in [ROOM NAME] - [brief description]

REQUIREMENTS:
- Add these items to the "items" list in their respective rooms
- Items should be pickable via "take [item]" command
- Items should appear in inventory when collected
- Keep item names short (1-2 words)

CODE STYLE:
- Simple Python, just adding to existing lists
- Comment which items were added where

Please show me the updated room entries with items added.
```

### For Items With Special Properties

```
I'm working on Castle Escape, a Python text adventure game with:
- Inventory system (can take/drop items)
- Room navigation
- [OTHER FEATURES YOU HAVE]

I want to add items with special properties and descriptions.

ITEM DETAILS:
Name: [ITEM NAME]
Location: [ROOM NAME]
Description: [What it looks like when examined]
Special property: [What makes it special - e.g., "heals 20 health", "glows in dark"]
How it's used: [What command or situation triggers its special property]

REQUIREMENTS:
1. Add item to room's item list
2. Add "examine [item]" command to show description
3. Add special behavior when item is used (if applicable)
4. Give feedback when player interacts with item

CODE STYLE:
- Simple Python suitable for beginners
- Clear comments explaining the special behavior
- Helpful messages to guide player

Please provide:
1. Item added to room
2. Examine command code
3. Special behavior code (if any)
4. Example of how player would interact with it
```

## 📝 Example Prompts

### Example 1: Adding Simple Collectibles

```
I'm working on Castle Escape with an inventory system.

I want to add collectible treasure items.

ITEMS TO ADD:
1. "gold coin" in dungeon - lying in the corner
2. "silver goblet" in hallway - on a shelf
3. "ruby ring" in courtyard - hidden in the fountain
4. "ancient crown" in library - on a pedestal

REQUIREMENTS:
- Add to room "items" lists
- Collectible via "take [item]"
- No special properties, just collectibles

Please show the updated rooms dictionary entries.
```

### Example 2: Adding a Usable Item

```
I'm working on Castle Escape with inventory and combat systems.

I want to add a healing potion.

ITEM DETAILS:
Name: "healing potion"
Location: library
Description: "A small glass bottle filled with glowing red liquid. It looks magical."
Special property: Restores 30 health when used
How it's used: Player types "use potion" when it's in inventory

REQUIREMENTS:
1. Add potion to library items list
2. Add "examine potion" to show description
3. Add "use potion" command that:
   - Checks if potion is in inventory
   - Restores 30 health
   - Removes potion from inventory (consumed)
   - Shows message about health restored
4. Can only use once (single-use consumable)

Please provide code for all parts of this item's functionality.
```

## 🧪 Testing Checklist

After adding items:

### Basic Functionality
- [ ] Items appear in their rooms initially
- [ ] Can pick up items with "take [item]"
- [ ] Items appear in inventory
- [ ] Can drop items with "drop [item]"
- [ ] Dropped items appear in current room

### Special Properties (if applicable)
- [ ] "examine [item]" shows description
- [ ] "use [item]" triggers special behavior
- [ ] Items with limited uses are removed when depleted
- [ ] Error messages when trying to use items you don't have
- [ ] Special items work correctly with other systems (combat, puzzles, etc.)

### Game Balance
- [ ] Items are distributed fairly
- [ ] Powerful items aren't too easy to find
- [ ] Items make sense in their locations
- [ ] Item count isn't overwhelming

## 💭 Understanding the Code

Make sure you understand:

1. **Where items are stored initially:** In the room's `"items": []` list

2. **How items transfer:** Removed from room list, added to inventory list

3. **Item checking:**
   ```python
   if "healing potion" in inventory:
       # Can use it
   ```

4. **Removing used items:**
   ```python
   inventory.remove("healing potion")
   ```

## 🎨 Extension Ideas

### 🟢 Easy Extensions
- Add flavor text when picking up each item
- Items that make sounds ("The coin clinks in your pocket")
- Hidden items that only appear after certain actions
- Items that give hints about puzzles

### 🟡 Medium Extensions
- **Examine system:** Detailed descriptions for every item
- **Item categories:** Quest items, weapons, treasures, consumables
- **Weight limit:** Can only carry so much
- **Item combinations:** Combine rope + hook = grappling hook
- **Quest items:** Must collect certain items to win
- **Key items:** Can't drop them (important for puzzles)

### 🔴 Advanced Extensions
- **Item durability:** Weapons break after X uses
- **Container items:** Backpack holds more items
- **Equipable items:** Wear armor, wield weapons
- **Crafting system:** Combine multiple items to create new ones
- **Item trading:** NPCs who swap items
- **Stackable items:** 3 torches stack, but 3 swords don't

## 🎮 Item Design Ideas

### By Room Type

**Dungeon/Prison:**
- Rusty chains, old bones, moldy bread, loose stone, prisoner's note

**Library:**
- Ancient books, scrolls, quill pen, reading glasses, bookmarks, maps

**Kitchen:**
- Cooking knife, food items, plates, cooking pot, recipe scroll

**Armory:**
- Swords, shields, bows, arrows, armor pieces, whetstones

**Treasury:**
- Gold, jewels, crowns, valuable art, deeds, money bags

**Alchemy Lab:**
- Potions, ingredients, mortar and pestle, vials, recipe books

**Garden:**
- Flowers, herbs, gardening tools, seeds, watering can

**Bedroom:**
- Jewelry, clothing, personal items, diary, love letters

## 🐛 Common Issues and Solutions

### Issue: Item has typo or wrong name
**Problem:** "rusty_key" vs "rusty key" inconsistency  
**Solution:** Use exact same string everywhere, check with print statements

### Issue: Can't pick up item that's clearly there
**Problem:** Item name doesn't match what you type  
**Solution:** Check for extra spaces, capitals, spelling

### Issue: Used item still in inventory
**Problem:** Forgot to remove it after use  
**Solution:** `inventory.remove(item_name)` after using consumable

### Issue: Item gives error when examined
**Problem:** Examine code isn't checking if item exists first  
**Solution:** Add `if item in inventory or item in room["items"]:`

### Issue: Items appear in wrong rooms
**Problem:** Added to wrong room's items list  
**Solution:** Double-check which room dictionary entry you modified

## 📚 Learning Reflections

After adding items, discuss:

1. **Game Design**
   - What makes an item interesting vs. boring?
   - How do items create gameplay opportunities?
   - What's the right amount of items?

2. **Organization**
   - How do we keep track of many items?
   - When would dictionaries be better than lists?
   - How do we prevent item name conflicts?

3. **Player Experience**
   - Where should powerful items be placed?
   - How do items guide player exploration?
   - What items are essential vs. optional?

## 🎯 Next Steps

Once you have a good set of items:

1. ✅ Try `01_adding_features/add_locked_door.md` - Use keys you created
2. ✅ Try `01_adding_features/add_combat_system.md` - Use weapons you created
3. ✅ Try `03_improving_gameplay/add_scoring_system.md` - Award points for treasures
4. ✅ Create item-based puzzles (combine items, use in specific places)

## 🎓 Teacher Notes

**Class Time:** 20-30 minutes

**Learning Objectives:**
- Understand data organization (lists, dictionaries)
- Think about game balance and design
- Practice extending existing systems
- Creative thinking about game mechanics

**Discussion Questions:**
- "What's your favorite item in a game you've played? Why?"
- "How do items make exploration more interesting?"
- "What's the difference between a key and a treasure?"
- "How would you organize items in a complex game?"

**Common Student Mistakes:**
- Inconsistent item names (capitals, spaces)
- Too many items (overwhelming)
- Items that don't make thematic sense
- Forgetting to remove consumable items after use
- No variation (all items are the same type)

**Group Activity:**
- Each student designs 2-3 items
- Class votes on most creative
- Add winning items to shared game
- Discuss what makes items fun

**Cross-Curricular:**
- **History:** Research medieval items that could be in a castle
- **Art:** Draw or describe items visually
- **Writing:** Create item descriptions and backstories
- **Economics:** Item value and trading systems

---

**Items bring your world to life!** Every item is an opportunity for creativity, storytelling, and gameplay. Think about what makes each item special and how it fits into your adventure. 💎✨
