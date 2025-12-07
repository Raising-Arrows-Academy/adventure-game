# 🐛 Debug Error Messages

## Overview
Learn how to use AI to help debug error messages in your code! This guide teaches you how to provide error information to AI assistants effectively and understand the solutions they provide.

## Difficulty
🔴 **When You Need It** - Errors happen to everyone, this helps you fix them!

## Prerequisites
- ✅ You encountered an error message
- ✅ You know which file/feature is causing the error
- ✅ You're ready to learn from the debugging process

## Python Concepts You'll Learn
- 📌 **Reading error messages** - Understanding what Python is telling you
- 📌 **Tracebacks** - Following the error path
- 📌 **Common error types** - Recognizing different kinds of errors
- 📌 **Debugging strategies** - Systematic problem-solving

## 🎯 Common Python Error Types

### SyntaxError
**What it means:** You wrote code that Python can't understand (typo, missing punctuation)

**Examples:**
```
SyntaxError: invalid syntax
SyntaxError: unexpected EOF while parsing
SyntaxError: unmatched ')'
```

**Common causes:**
- Missing colon `:` after if, while, def
- Unmatched quotes, parentheses, or brackets
- Wrong indentation

### NameError
**What it means:** You used a variable or function that doesn't exist

**Examples:**
```
NameError: name 'scor' is not defined
NameError: name 'Random' is not defined
```

**Common causes:**
- Typo in variable name
- Variable not created yet
- Wrong capitalization

### KeyError
**What it means:** You tried to access a dictionary key that doesn't exist

**Examples:**
```
KeyError: 'nroth'
KeyError: 'items'
```

**Common causes:**
- Typo in dictionary key
- Key doesn't exist in that dictionary
- Wrong dictionary being accessed

### IndexError
**What it means:** You tried to access a list item that doesn't exist

**Examples:**
```
IndexError: list index out of range
```

**Common causes:**
- List is shorter than you think
- Using wrong index number
- Empty list

### TypeError
**What it means:** You used a value in a way that doesn't work with its type

**Examples:**
```
TypeError: can only concatenate str (not "int") to str
TypeError: 'int' object is not subscriptable
```

**Common causes:**
- Mixing strings and numbers incorrectly
- Calling something that's not a function
- Using wrong type in operation

### IndentationError
**What it means:** Your indentation (spacing) is wrong

**Examples:**
```
IndentationError: expected an indented block
IndentationError: unexpected indent
```

**Common causes:**
- Mixing tabs and spaces
- Wrong number of spaces
- Code not lined up correctly

## 🎯 The Debug Prompt Template

When you get an error, use this template:

```
I'm working on Castle Escape, a Python text adventure game. I'm a beginner.

I'm getting an error and need help debugging.

ERROR INFORMATION:

Error Type: [Copy the error type from the message]

Full Error Message:
```
[Paste the COMPLETE error message here, including the traceback]
```

WHAT I WAS TRYING TO DO:
[Explain what you were trying to accomplish when the error occurred]

RELEVANT CODE:
```python
[Paste the section of code where the error occurs - include line numbers if possible]
```

WHAT I'VE TRIED:
[List anything you've already tried to fix it]

Please explain:
1. What the error means in beginner-friendly terms
2. What's causing this specific error in my code
3. How to fix it
4. How to avoid this error in the future

Use simple language suitable for a Python beginner.
```

## 📝 Example Debug Prompts

### Example 1: NameError

```
I'm working on Castle Escape. I'm getting an error when trying to add a score system.

ERROR INFORMATION:

Error Type: NameError

Full Error Message:
```
Traceback (most recent call last):
  File "castle_escape.py", line 67, in <module>
    main()
  File "castle_escape.py", line 45, in main
    scor += 10
NameError: name 'scor' is not defined
```

WHAT I WAS TRYING TO DO:
I was adding a score system. When the player picks up an item, I want to add 10 points
to their score.

RELEVANT CODE:
```python
# Line 12: At the start of main()
score = 0

# Line 45: When player picks up item
if command.startswith("take"):
    item = command.split()[1]
    if item in rooms[current_room]["items"]:
        inventory.append(item)
        rooms[current_room]["items"].remove(item)
        scor += 10  # <-- ERROR ON THIS LINE
        print(f"You picked up the {item}. +10 points!")
```

WHAT I'VE TRIED:
I checked that score is created at the start. I'm not sure why it says it's not defined.

Please help me understand and fix this error!
```

### Example 2: KeyError

```
I'm working on Castle Escape. I'm getting an error when I try to go north from the hallway.

ERROR INFORMATION:

Error Type: KeyError

Full Error Message:
```
Traceback (most recent call last):
  File "castle_escape.py", line 78, in <module>
    main()
  File "castle_escape.py", line 52, in main
    next_room = rooms[current_room][command]
KeyError: 'nroth'
```

WHAT I WAS TRYING TO DO:
I tried to move north from the hallway to the courtyard.

RELEVANT CODE:
```python
# In the movement section
if command in ["north", "south", "east", "west", "n", "s", "e", "w"]:
    if command in rooms[current_room]:
        next_room = rooms[current_room][command]
        current_room = next_room
    else:
        print("You can't go that way!")
```

WHAT I'VE TRIED:
I checked the rooms dictionary and "north" is definitely an exit from hallway. I'm confused
why it's looking for "nroth" instead of "north".

Please help!
```

## 🧪 Debugging Checklist

When you encounter an error:

### Before Asking AI
- [ ] Read the error message completely
- [ ] Find the line number where error occurred
- [ ] Look at that line of code carefully
- [ ] Check for obvious typos
- [ ] Make sure you saved your file
- [ ] Try running the code again (sometimes it was a temporary glitch)

### When Asking AI
- [ ] Copy the COMPLETE error message (including traceback)
- [ ] Include the relevant code section
- [ ] Explain what you were trying to do
- [ ] Mention what you've already tried
- [ ] Specify you're a beginner

### After Getting Help
- [ ] Read the explanation carefully
- [ ] Understand WHY the error happened
- [ ] Apply the fix
- [ ] Test that it works
- [ ] Try to break it again (learn the boundaries)
- [ ] Remember this for next time

## 💭 Understanding Error Messages

### Anatomy of an Error Message

```
Traceback (most recent call last):          ← Shows the path to the error
  File "castle_escape.py", line 67          ← Which file
    main()                                   ← Which function
  File "castle_escape.py", line 45          ← Where in that function
    scor += 10                               ← The actual line with the problem
NameError: name 'scor' is not defined       ← What went wrong
```

**Read from bottom to top:**
1. Start with the error type and message
2. Look at the line of code it points to
3. Follow the traceback up if needed

## 🎨 Self-Debugging Strategies

Before asking AI, try these:

### 1. Read the Error Message Carefully
- What type of error is it?
- What line number?
- What does the message say?

### 2. Check the Obvious
- Typos (scor vs score)
- Capitalization (Score vs score)
- Missing punctuation (: after if)
- Indentation

### 3. Use Print Debugging
```python
print(f"Current room: {current_room}")
print(f"Command: {command}")
print(f"Rooms dictionary: {rooms}")
```

### 4. Comment Out Code
- Comment out new code to find what broke
- Uncomment piece by piece to isolate problem

### 5. Compare to Working Code
- Look at similar code that works
- What's different?

## 🐛 Common Beginner Errors and Quick Fixes

### Forgot Colon
```python
# ❌ Wrong
if command == "north"
    print("Going north")

# ✅ Correct
if command == "north":
    print("Going north")
```

### Wrong Indentation
```python
# ❌ Wrong
def show_room():
print("Room description")

# ✅ Correct
def show_room():
    print("Room description")
```

### Typo in Variable Name
```python
# ❌ Wrong
score = 0
scor += 10  # Typo!

# ✅ Correct
score = 0
score += 10
```

### Missing Quotes
```python
# ❌ Wrong
room = dungeon  # Python thinks dungeon is a variable

# ✅ Correct
room = "dungeon"  # It's a string
```

### Mixing Types
```python
# ❌ Wrong
score = "0"
score += 10  # Can't add number to string

# ✅ Correct
score = 0
score += 10
```

## 📚 Learning Reflections

After debugging:

1. **What caused the error?**
   - Write down what you learned

2. **How could you prevent it next time?**
   - What warning signs were there?

3. **What debugging technique worked?**
   - Remember for future issues

4. **Did the error message help?**
   - Learn to read Python's clues

## 🎯 Next Steps

After fixing your error:

1. ✅ Test thoroughly to make sure it's really fixed
2. ✅ Try `05_debugging/fix_logic_bug.md` if code runs but does wrong thing
3. ✅ Keep a "debug log" of errors you've fixed
4. ✅ Help classmates with similar errors

## 🎓 Teacher Notes

**Teaching Moment:** Errors are learning opportunities!

**Learning Objectives:**
- Read and understand error messages
- Develop systematic debugging skills
- Learn to ask for help effectively
- Build resilience and problem-solving

**Discussion Questions:**
- "What does this error message tell us?"
- "Where should we start looking?"
- "What could cause this error?"
- "How can we prevent this in the future?"

**Common Student Issues:**
- Panic when seeing errors
- Not reading the full error message
- Changing random things hoping to fix it
- Giving up too quickly
- Not learning from the fix

**Classroom Debugging Activity:**
1. Show error on screen
2. Read error message together
3. Identify error type
4. Locate problem line
5. Brainstorm causes
6. Fix and test
7. Discuss prevention

**Growth Mindset:**
- Everyone gets errors (even professionals!)
- Errors are how we learn
- Good programmers are good debuggers
- Each error makes you better

**Debug Log:**
Have students keep a log:
- Date
- Error type
- What caused it
- How they fixed it
- What they learned

---

**Errors are your teachers!** Every error you fix makes you a better programmer. Don't get discouraged - debugging is a core programming skill that you're developing. Stay patient, read carefully, and learn from each mistake! 🐛✨
