# 🏆 Add Scoring System

## Overview
Add a point system to track player achievements! Award points for collecting items, defeating enemies, solving puzzles, and completing objectives. This adds goals and replayability to your game.

## Difficulty
🟢 **Easy** - Simple variable tracking with fun rewards!

## Prerequisites
- ✅ Base game is working
- ✅ You understand variables and how to add/subtract numbers
- ✅ You have some actions to award points for (collecting items, defeating enemies, etc.)

## Python Concepts You'll Learn
- 📌 **Score tracking** - Using a variable to accumulate points
- 📌 **Arithmetic operations** - Adding points with `+=`
- 📌 **Conditional rewards** - Award points for specific achievements
- 📌 **Display formatting** - Showing score nicely

## 🎯 The Prompt

Copy this prompt and paste it into your AI assistant:

```
I'm working on Castle Escape, a Python text adventure game for beginners.

I have working:
- Room navigation system
- [LIST OTHER FEATURES: inventory, combat, locked doors, etc.]

I want to add a scoring system to track player achievements.

REQUIREMENTS:

SCORE TRACKING:
1. Create a 'score' variable starting at 0
2. Display current score in game status or on command

AWARD POINTS FOR:
- Picking up treasures/items: 10 points each
- Defeating an enemy: 25 points
- Unlocking a door: 15 points
- Discovering a new room: 5 points (first time only)
- Escaping the castle (winning): 100 points
- [ADD YOUR OWN: any other achievements you want to reward]

DISPLAY:
- Add 'score' command to show current score
- Show score automatically after earning points
- Display final score when game ends (win or lose)
- Optional: Show score in status bar or room header

BONUS FEATURES (optional):
- Track high score (best score achieved)
- Award ranks (0-50: Beginner, 51-100: Explorer, 101+: Master)
- Show points earned for each action
- Save high score between games (if save/load exists)

CODE STYLE:
- Use simple Python (one integer variable for score)
- NO classes or complex structures
- Add clear comments
- Show encouraging messages when points are earned

Please provide:
1. Score variable initialization
2. Code to award points for different actions
3. Score display command
4. Final score display at game end
5. Where to integrate into existing code
```

## 🧪 Testing Checklist

After adding the scoring system:

### Basic Functionality
- [ ] Score starts at 0
- [ ] Type `score` - displays current score
- [ ] Pick up an item - score increases and shows message
- [ ] Perform other point-worthy actions - score increases
- [ ] Score persists throughout game (doesn't reset)

### Point Awards
- [ ] Each point-earning action awards correct amount
- [ ] Can't earn points twice for same action (e.g., same item)
- [ ] Points awarded at the right time
- [ ] Messages confirm points earned

### End Game
- [ ] Win the game - final score displays
- [ ] Lose (if applicable) - final score displays
- [ ] Score total makes sense for actions taken

### High Score (if implemented)
- [ ] High score saves between game sessions
- [ ] Beating high score shows congratulations message
- [ ] High score displays when viewing score

## 💭 Understanding the Code

After AI gives you the code, make sure you can answer:

1. **Where is score initialized?** (Before main loop: `score = 0`)
2. **How do we add points?** (`score += 10` or `score = score + 10`)
3. **How do we prevent double-counting?** (Check if already done before awarding)
4. **Where is score displayed?** (On `score` command, after earning points, at game end)
5. **How is high score tracked?** (Compare current to high, update if higher)

### Example Code Discussion Points

Look for these patterns:

```python
# Initialize score
score = 0

# Award points
score += 10
print("You found treasure! +10 points!")

# Display score
if command == "score":
    print(f"Current score: {score}")

# End game score
print(f"\nFinal Score: {score}")
```

## 🎨 Extension Ideas

Once basic scoring works, try these:

### 🟢 Easy Extensions
- **Point values for more actions:**
  - Reading books (+2)
  - Helping NPCs (+20)
  - Completing quests (+50)
  - Finding secrets (+25)

- **Score display options:**
  - Always visible in status bar
  - Different color for point messages
  - Show points breakdown (Items: 40, Enemies: 25, Exploration: 15)

- **Rank system:**
  ```
  0-25:    Novice Adventurer
  26-75:   Skilled Explorer
  76-150:  Castle Master
  151+:    Legendary Hero
  ```

### 🟡 Medium Extensions
- **Multipliers:**
  - Speed bonus (complete quickly)
  - Efficiency bonus (minimal moves)
  - Perfect play bonus (no damage taken)

- **Achievements:**
  - Specific goals worth bonus points
  - "Pacifist" - escape without fighting
  - "Collector" - find all items
  - "Speed Runner" - win in under 20 moves

- **Penalties:**
  - Lose points for dying (-10)
  - Lose points for giving up
  - Lose points over time (time pressure)

- **High score table:**
  - Top 5 scores saved
  - With player name
  - With date achieved

### 🔴 Advanced Extensions
- **Point shop:**
  - Spend points on hints
  - Buy healing or items
  - Unlock bonus content

- **Score-based unlocks:**
  - High score unlocks new game mode
  - Unlock special items or rooms
  - Unlock different difficulty levels

- **Combo system:**
  - Multiple quick actions = more points
  - Chains of related actions
  - Perfect runs multiply points

## 🐛 Common Issues and Solutions

### Issue: Score resets during game
**Problem:** Score variable created inside main loop  
**Solution:** Initialize `score = 0` BEFORE the main game loop

### Issue: Can earn infinite points from same action
**Problem:** No check if already done  
**Solution:** Use boolean flags:
```python
if item not in collected_items:
    score += 10
    collected_items.append(item)
```

### Issue: Negative score possible
**Problem:** Penalties without lower limit  
**Solution:** Check before subtracting:
```python
if score >= 10:
    score -= 10
else:
    score = 0
```

### Issue: High score doesn't save
**Problem:** Not using file I/O to persist data  
**Solution:** Requires save/load system (see that prompt)

### Issue: Score shows at wrong times
**Problem:** Print statements in wrong places  
**Solution:** Be intentional about when score displays

## 📊 Point Balance Guide

How many points should things be worth?

**Small achievements:** 5-10 points
- Finding new room
- Reading a note
- Simple interactions

**Medium achievements:** 15-25 points
- Collecting items
- Solving easy puzzles
- Unlocking doors

**Major achievements:** 30-50 points
- Defeating enemies
- Solving complex puzzles
- Completing quests

**Ultimate achievements:** 75-100+ points
- Beating the game
- Perfect completion
- Special challenges

**Total possible points:** Calculate maximum score if player does everything, use that to create ranks.

## 📚 Learning Reflections

After adding scoring, discuss:

1. **Variable Operations**
   - How does `+=` work?
   - What's the difference between `=` and `+=`?
   - How do we accumulate values over time?

2. **Game Design**
   - What motivates players to get high scores?
   - How do points create goals?
   - What's the right balance of easy vs. hard points?

3. **Feedback**
   - Why show points earned immediately?
   - How do points make players feel accomplished?
   - What makes a satisfying point system?

## 🎯 Next Steps

Once scoring works well:

1. ✅ Try `03_improving_gameplay/add_save_load.md` - Save high scores
2. ✅ Add more point-earning opportunities
3. ✅ Create achievements or challenges
4. ✅ Add difficulty levels with score multipliers

## 🎓 Teacher Notes

**Class Time:** 20-30 minutes

**Learning Objectives:**
- Understand variable accumulation
- Practice arithmetic operations
- Think about game balance
- Create player motivation systems

**Discussion Questions:**
- "What makes a good scoring system?"
- "Would you rather have few big rewards or many small ones?"
- "How do high scores change how you play?"
- "What games have you played with good scoring?"

**Common Student Mistakes:**
- Score variable inside loop (resets)
- No validation (can cheat infinite points)
- Points too easy or too hard to get
- No feedback when points earned
- Forgetting to display final score

**Math Connection:**
- Adding and accumulating
- Planning point economy
- Calculating percentages (score/max_score)
- Statistical analysis of playthroughs

**Extension Activity:**
**Score Design Challenge**
- Students design point system for their game
- Calculate maximum possible score
- Create rank tiers
- Balance risk vs. reward
- Test with classmates and adjust

**Gamification:**
This feature teaches game design principle of "extrinsic motivation" - external rewards. Discuss:
- Intrinsic (fun) vs. Extrinsic (points) motivation
- Which is more important?
- How do they work together?

---

**Points make games more rewarding!** A well-designed scoring system gives players goals, feedback, and reasons to replay. Think about what actions deserve recognition! 🏆✨
