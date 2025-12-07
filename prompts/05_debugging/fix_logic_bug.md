# 🔧 Fix Logic Bugs

## Overview
Learn how to debug code that runs without errors but does the WRONG thing! Logic bugs are when your code works, but not the way you intended. This guide helps you describe problems to AI and fix logical errors.

## Difficulty
🔴 **When You Need It** - Logic bugs can be tricky, but you can fix them!

## Prerequisites
- ✅ Your code runs without crashing (no error messages)
- ✅ You know what you WANT to happen
- ✅ You can see what ACTUALLY happens
- ✅ You can explain the difference

## Python Concepts You'll Learn
- 📌 **Logic flow** - Following how code executes
- 📌 **Conditional logic** - Understanding if/elif/else chains
- 📌 **State tracking** - Watching how variables change
- 📌 **Expected vs. actual behavior** - Systematic testing

## 🎯 What Are Logic Bugs?

**Logic bugs** occur when:
- Code runs without errors ✓
- But it does the wrong thing ✗

### Examples

**Problem:** "I can pick up the same item infinite times"  
**Logic bug:** Not removing item from room after taking it

**Problem:** "Door unlocks but I still can't go through"  
**Logic bug:** Movement code checks old locked state

**Problem:** "Score goes up when I DON'T defeat enemy"  
**Logic bug:** Score increases in wrong place in code

**Problem:** "Inventory shows items I dropped"  
**Logic bug:** Not removing from inventory list

## 🎯 The Logic Bug Prompt Template

```
I'm working on Castle Escape, a Python text adventure game. I'm a beginner.

I have a logic bug - my code runs without errors but doesn't work correctly.

WHAT I EXPECT TO HAPPEN:
[Describe in detail what SHOULD happen]

WHAT ACTUALLY HAPPENS:
[Describe in detail what ACTUALLY happens instead]

RELEVANT CODE:
```python
[Paste the section of code that you think is related to the problem]
```

STEPS TO REPRODUCE:
1. [First action]
2. [Second action]
3. [Third action]
4. [Buggy behavior occurs]

WHAT I'VE TRIED:
[List any debugging steps you've already taken]

GAME STATE:
- Inventory: [what's in inventory]
- Current room: [where player is]
- Other relevant variables: [any other state that matters]

Please help me:
1. Identify what's wrong with my logic
2. Explain why it's happening
3. Show me how to fix it
4. Suggest how to test the fix

Use beginner-friendly language.
```

## 📝 Example Logic Bug Prompts

### Example 1: Items Don't Stay Taken

```
I'm working on Castle Escape with an inventory system.

I have a logic bug with items.

WHAT I EXPECT TO HAPPEN:
When I type "take key", the key should:
- Be removed from the room
- Be added to my inventory
- Not be available to take again in that room

WHAT ACTUALLY HAPPENS:
- Key gets added to inventory ✓
- But it's still in the room
- I can type "take key" again and get another copy
- My inventory has multiple of the same key

RELEVANT CODE:
```python
if command.startswith("take"):
    parts = command.split()
    if len(parts) >= 2:
        item = parts[1]
        if item in rooms[current_room]["items"]:
            inventory.append(item)
            print(f"You picked up the {item}.")
        else:
            print(f"There is no {item} here.")
```

STEPS TO REPRODUCE:
1. Start game in dungeon (key is here)
2. Type "take key" - works, key in inventory
3. Type "take key" again - works again! Now have 2 keys
4. Can repeat infinitely

WHAT I'VE TRIED:
- Checked that item is in room (it is)
- Checked that it's being added to inventory (it is)
- Confused why it's not removed from room

Please help me understand what's missing!
```

### Example 2: Door Won't Unlock

```
I'm working on Castle Escape with locked doors.

I have a logic bug with the locked door.

WHAT I EXPECT TO HAPPEN:
- Door between hallway and courtyard starts locked
- When I have the key and try to go north, it should unlock
- After unlocking, I should be able to go through
- Door should stay unlocked

WHAT ACTUALLY HAPPENS:
- Door starts locked ✓
- When I try to go north with key, message says "You unlock the door!"
- But then it IMMEDIATELY says "The door is locked!"
- I don't move to the next room
- Door seems to unlock and re-lock instantly

RELEVANT CODE:
```python
if command == "north" and current_room == "hallway":
    if door_locked:
        if "rusty key" in inventory:
            print("You use the rusty key to unlock the door!")
            door_locked = False
        print("The door is locked. You need a key!")
    else:
        current_room = "courtyard"
        show_room(current_room, rooms)
```

STEPS TO REPRODUCE:
1. Start game, get to hallway
2. Go back, get key from dungeon
3. Return to hallway
4. Type "north"
5. See unlock message, then immediately locked message
6. Still in hallway, not courtyard

WHAT I'VE TRIED:
- Verified I have the key (I do)
- Checked variable name is correct
- Checked that door_locked is set to False
- Still not working

Help please!
```

### Example 3: Combat Keeps Going After Victory

```
I'm working on Castle Escape with a combat system.

I have a logic bug during combat.

WHAT I EXPECT TO HAPPEN:
- Fight enemy until their health reaches 0
- When enemy health hits 0, combat should end
- Victory message should show
- Should return to normal game mode

WHAT ACTUALLY HAPPENS:
- Can attack enemy normally ✓
- Enemy health goes down ✓
- When enemy health hits 0, victory message shows ✓
- BUT then enemy attacks me anyway!
- Combat doesn't end
- Enemy at 0 health can still hit me

RELEVANT CODE:
```python
while True:
    action = input("Attack or Run? > ").lower()
    
    if action == "attack":
        damage = random.randint(5, 15)
        enemy_health -= damage
        print(f"You hit for {damage} damage!")
        
        if enemy_health <= 0:
            print("You defeated the enemy!")
            break
        
        enemy_damage = random.randint(3, 10)
        player_health -= enemy_damage
        print(f"Enemy hits you for {enemy_damage} damage!")
```

STEPS TO REPRODUCE:
1. Enter room with enemy
2. Attack until enemy health is very low
3. Attack one more time, reducing enemy health to -5
4. See "You defeated the enemy!" message
5. See enemy still attacking me
6. Combat continues

WHAT I'VE TRIED:
- Checked the break statement (it's there)
- Checked if enemy_health <= 0 (it is)
- Not sure why enemy still attacks

Please help me figure out the logic problem!
```

## 🧪 Debugging Logic Bugs Checklist

### Step 1: Reproduce the Bug
- [ ] Can you make the bug happen reliably?
- [ ] Write down exact steps that cause it
- [ ] Note what state the game is in when it happens

### Step 2: Identify Expected vs. Actual
- [ ] What did you expect to happen?
- [ ] What actually happened?
- [ ] What's the specific difference?

### Step 3: Find the Relevant Code
- [ ] Which part of code handles this feature?
- [ ] Which function or section is involved?
- [ ] What variables are being used?

### Step 4: Add Print Statements
- [ ] Print variable values at key points
- [ ] Print when entering/exiting if statements
- [ ] Print to see which code path executes

### Step 5: Trace the Logic
- [ ] Follow the code line by line in your mind
- [ ] What's the value of each variable at each step?
- [ ] Which if statements evaluate to True vs. False?

### Step 6: Fix and Test
- [ ] Make the fix
- [ ] Test the exact scenario that was broken
- [ ] Test related scenarios
- [ ] Test edge cases

## 💭 Common Logic Bug Patterns

### Pattern 1: Forgotten State Update
**Symptom:** Action happens but state doesn't change

**Example:**
```python
# Taking item but not removing from room
inventory.append(item)  # ✓ Added to inventory
# ✗ MISSING: rooms[current_room]["items"].remove(item)
```

**Fix:** Update all related state

### Pattern 2: Wrong Condition Order
**Symptom:** Later conditions never execute

**Example:**
```python
# ❌ Wrong order
if door_locked:
    if "key" in inventory:
        door_locked = False
    print("Door is locked!")  # Always prints!
```

**Fix:** Check unlocked condition AFTER updating state

### Pattern 3: Condition Too Broad/Narrow
**Symptom:** Code runs when it shouldn't (or vice versa)

**Example:**
```python
# ❌ Too broad - runs for ALL commands starting with "t"
if command.startswith("t"):
    # Meant for "take" but also triggers for "talk", "turn", etc.
```

**Fix:** Be specific with conditions

### Pattern 4: Variable Not Updated
**Symptom:** Using old value instead of new value

**Example:**
```python
# ❌ Using local variable instead of updating global
def unlock_door():
    door_locked = False  # Local variable!
    # Doesn't affect the global door_locked
```

**Fix:** Use global keyword or return value

### Pattern 5: Off-by-One Errors
**Symptom:** Stopping too early or going too far

**Example:**
```python
# ❌ Misses last item
for i in range(len(inventory) - 1):  # Should be range(len(inventory))
```

**Fix:** Check loop boundaries carefully

## 🔍 Debug Techniques

### Print Debugging
```python
print(f"DEBUG: current_room = {current_room}")
print(f"DEBUG: command = {command}")
print(f"DEBUG: Entering if statement")
```

Remove these prints after debugging!

### Rubber Duck Debugging
Explain your code out loud (to a rubber duck, pet, or friend):
- "When the player types 'take key'..."
- "The code checks if key is in the room..."
- "Then it adds key to inventory..."
- "Wait, I never remove it from the room!"

Often, explaining reveals the problem!

### Simplified Test Case
Reduce to minimum code that shows the bug:
```python
# Instead of full game, test just the problematic function
inventory = []
room_items = ["key"]

# Test take logic
inventory.append("key")
print(f"Inventory: {inventory}")
print(f"Room items: {room_items}")
# See the problem: room_items still has "key"!
```

## 📚 Learning Reflections

After fixing a logic bug:

1. **What was the actual problem?**
   - Write it down in simple terms

2. **Why did the bug exist?**
   - What was the logical mistake?

3. **How did you find it?**
   - Which debugging technique worked?

4. **How can you prevent it?**
   - What should you check next time?

## 🎯 Next Steps

After fixing your logic bug:

1. ✅ Test thoroughly in multiple scenarios
2. ✅ Check for similar bugs in related code
3. ✅ Try `05_debugging/debug_error.md` for error messages
4. ✅ Keep a log of bugs you've fixed

## 🎓 Teacher Notes

**Teaching Opportunity:** Logic bugs teach critical thinking!

**Learning Objectives:**
- Develop systematic debugging approach
- Practice tracing code execution
- Learn to test thoroughly
- Build problem-solving resilience

**Discussion Questions:**
- "Why does the code do what it does?"
- "What did we expect? What happened? What's different?"
- "How can we test each piece?"
- "What questions should we ask?"

**Debugging Process:**
1. Reproduce reliably
2. Identify expected vs. actual
3. Form hypothesis
4. Test hypothesis
5. If wrong, form new hypothesis
6. If right, implement fix
7. Test fix thoroughly

**Common Student Challenges:**
- Random changes hoping to fix
- Not testing systematically
- Not reading code carefully
- Giving up too quickly
- Assuming AI code is perfect

**Class Debugging Activity:**
Present intentional logic bug:
1. Show code
2. Describe expected vs. actual
3. Students brainstorm causes
4. Test hypotheses together
5. Find and fix bug
6. Discuss what we learned

**Growth Mindset:**
- Logic bugs are puzzles to solve
- Professional programmers debug constantly
- Each bug solved improves skills
- Frustration is part of learning

---

**Logic bugs make you think!** They're sometimes harder than syntax errors because the code "works" - just not correctly. Take your time, be systematic, and celebrate when you find the problem! 🔧✨
