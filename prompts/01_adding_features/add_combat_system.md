# ⚔️ Add Combat System

## Overview
Add enemy encounters and a combat system where players can fight enemies using health tracking, attack commands, and random damage. This adds excitement and challenge to your adventure!

## Difficulty
🟡 **Medium** - Introduces random numbers and more complex state tracking

## Prerequisites
- ✅ Inventory system is working (used for weapons)
- ✅ You understand how variables track changing values
- ✅ You understand basic math operations in Python
- ✅ You're comfortable with if/elif/else statements

## Python Concepts You'll Learn
- 📌 **Random module** - `import random` and `random.randint()`
- 📌 **Variable tracking** - Player and enemy health
- 📌 **Math operations** - Calculating damage, updating health
- 📌 **Game loops** - Combat continues until someone wins
- 📌 **Win/lose conditions** - Checking if health reaches zero

## 🎯 The Prompt

Copy this prompt and paste it into your AI assistant:

```
I'm working on Castle Escape, a Python text adventure game for beginners.

I have working:
- Room navigation system
- Inventory system with items including a 'sword'
- Player can move around and collect items

I want to add a combat system. Here's what I need:

REQUIREMENTS:

HEALTH TRACKING:
1. Player starts with 100 health
2. Enemy (guard) has 50 health
3. Display current health during combat

COMBAT MECHANICS:
1. Add a 'guard' enemy in the hallway
2. When player enters room with enemy, start combat automatically
3. During combat, player can:
   - 'attack' or 'a' - attack the enemy (random damage 5-15 if has sword, 1-5 if no sword)
   - 'run' or 'r' - escape to previous room
4. After player attacks, enemy attacks back (random damage 3-10)
5. Show damage dealt and taken after each round
6. Combat continues until:
   - Player defeats enemy (enemy health <= 0) - enemy disappears, player continues
   - Player runs away (returns to previous room)
   - Player is defeated (player health <= 0) - game over, offer to restart

DISPLAY:
- Clear messages showing what's happening
- Health status after each action
- Victory/defeat messages

CODE STYLE:
- Use simple Python (variables, random, while loops, if/elif)
- Import random at the top: `import random`
- NO classes or complex structures  
- Add clear comments
- Use `random.randint(min, max)` for damage calculation

Please provide:
1. How to import and use the random module
2. Health variables and tracking
3. Combat loop structure
4. Enemy placement in room
5. Integration with existing game loop

Make it beginner-friendly and well-commented!
```

## 🧪 Testing Checklist

After adding the code, test these scenarios:

### Basic Combat
- [ ] Enter the hallway - combat should start automatically
- [ ] Type `attack` - should damage the enemy
- [ ] Enemy should attack back and damage you
- [ ] Both health totals should display after each round
- [ ] Continue attacking until enemy is defeated
- [ ] After victory, guard should be gone if you return

### Combat With/Without Weapon
- [ ] Fight without sword - should do less damage (1-5)
- [ ] Pick up sword, then fight - should do more damage (5-15)
- [ ] Damage numbers should be random (not always the same)

### Running Away
- [ ] Start combat
- [ ] Type `run` - should escape to previous room
- [ ] Guard should still be there if you go back

### Losing a Fight
- [ ] Let the enemy attack without fighting back (or debug by lowering your health)
- [ ] When health reaches 0, should get "game over" message
- [ ] Should offer to restart or quit

### Edge Cases
- [ ] Type invalid commands during combat - should prompt for valid command
- [ ] Defeat enemy with one hit if possible
- [ ] Make sure non-combat rooms still work normally

## 💭 Understanding the Code

After AI gives you the code, make sure you can answer these questions:

1. **Where is the random module imported?** (At the very top of the file)
2. **How does `random.randint(5, 15)` work?** (Returns random integer between 5 and 15)
3. **Where are health variables initialized?** (Before main game loop)
4. **How does combat loop work?** (While loop that continues while both alive)
5. **What breaks the combat loop?** (Enemy defeated, player defeated, or player runs)
6. **How is enemy tracked per room?** (Usually boolean flag or removed from room)
7. **Why subtract damage from health?** (Simulates taking damage)

### Example Code Discussion Points

Look for these patterns:

```python
import random  # At top of file

# Before game loop
player_health = 100
enemy_health = 50

# In combat
damage = random.randint(5, 15)  # Random damage
enemy_health -= damage  # Subtract from enemy

# Check win/lose
if enemy_health <= 0:
    print("You defeated the guard!")
if player_health <= 0:
    print("You have been defeated!")
```

## 🎨 Extension Ideas

Once basic combat works, try these modifications:

### 🟢 Easy Extensions
- Add healing items (potion restores 20 health)
- Different weapons do different damage (dagger: 3-8, sword: 5-15, axe: 8-20)
- Add more enemies in different rooms
- Show health bar visually: `[||||||||--]` 
- Enemy drops items when defeated

### 🟡 Medium Extensions
- Multiple enemies (fight them one at a time or all at once)
- Special attacks that cost health but do more damage
- Enemy has different attack types (guard vs. wizard)
- Armor that reduces damage taken
- Critical hits (random chance for double damage)
- Player can defend (take less damage that round)

### 🔴 Advanced Extensions
- Turn-based combat with stamina points
- Elemental damage types (fire, ice, lightning)
- Enemy AI with different behaviors
- Status effects (poison, stun, burn)
- Experience points and leveling up
- Multiple combat styles (magic, melee, ranged)

## 🐛 Common Issues and Solutions

### Issue: "NameError: random is not defined"
**Problem:** Forgot to import random module  
**Solution:** Add `import random` at the very top of your file

### Issue: Damage is always the same
**Problem:** Not using random.randint()  
**Solution:** Use `random.randint(min, max)` not just a fixed number

### Issue: Combat never ends
**Problem:** While loop condition might be wrong  
**Solution:** Check loop exits when `enemy_health <= 0` or `player_health <= 0`

### Issue: Can fight defeated enemy again
**Problem:** Not removing or flagging enemy as defeated  
**Solution:** Use boolean flag `guard_defeated = True` or remove enemy from room

### Issue: Negative health
**Problem:** Health goes below zero and keeps going  
**Solution:** This is okay! Or check `if health < 0: health = 0` after damage

### Issue: Enemy attacks after being defeated
**Problem:** Attack order might be wrong  
**Solution:** Check if enemy health > 0 BEFORE enemy attacks back

## 📚 Learning Reflections

After completing this feature, discuss:

1. **How does randomness make games fun?**
   - What if damage was always the same?
   - How does unpredictability create excitement?

2. **Variable state tracking**
   - How many different variables track game state?
   - What happens when health reaches zero?

3. **Loop structures**
   - How is a combat loop different from the main game loop?
   - When should the combat loop end?

4. **Math in games**
   - How does subtraction simulate damage?
   - What other math operations are used in games?

## 🎯 Next Steps

Once your combat system works perfectly:

1. ✅ Try `02_expanding_world/add_items.md` - Add weapons and healing potions
2. ✅ Try `03_improving_gameplay/add_scoring_system.md` - Award points for victories
3. ✅ Add multiple enemies with different stats
4. ✅ Create boss battle with higher health and damage

## 🎓 Teacher Notes

**Class Time:** 45-60 minutes

**Learning Objectives:**
- Understand random number generation
- Practice variable state management
- Learn nested loop structures
- Experience more complex conditional logic

**Discussion Questions:**
- "Why do we import random at the top of the file?"
- "How would you make combat more strategic?"
- "What happens if player health goes negative?"
- "How would you add a 'heal' command?"
- "What makes combat feel fair vs. unfair?"

**Common Student Mistakes:**
- Forgetting to import random
- Not checking if enemy is defeated before counter-attack
- Combat loop doesn't exit properly
- Negative health not handled
- Using random() instead of randint()
- Not resetting health when restarting

**Math Connection:**
- Discuss range of random numbers
- Probability of different damage amounts
- Expected value (average damage over time)
- Balance: Is combat too easy or too hard?

**Extension Activity:**
Challenge: Make combat tactical
- Add "defend" option (take half damage, don't attack)
- Add "special attack" (costs 10 health, does double damage)
- Students analyze which strategy is best mathematically

**Safety Note:**
While this is combat, keep it appropriate:
- No graphic descriptions
- Focus on fantasy/medieval theme
- Defeat means "knocked out" not killed
- Keep it fun and game-like

---

**Combat adds excitement!** This feature teaches important programming concepts like random numbers and state management. Remember: balance is key - make it challenging but fair! ⚔️✨
