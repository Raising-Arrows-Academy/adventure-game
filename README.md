# 🏰 Castle Escape - AI-Assisted Adventure Game

Welcome to **Castle Escape**! This is a text-based adventure game built collaboratively using Python and AI as a learning tool.

## 🎯 Project Overview

This project is designed to teach Python programming through an interactive, AI-assisted development approach. Students learn by:

- **Suggesting features** for the game
- **Working with AI** to implement those features
- **Reading and understanding** the generated code
- **Testing and debugging** to ensure everything works

### What You'll Learn

- ✅ Python programming fundamentals (variables, loops, functions, dictionaries)
- ✅ How to effectively use AI as a coding assistant
- ✅ Code comprehension and debugging skills
- ✅ Iterative software development
- ✅ Game design principles

---

## 🚀 Getting Started (Easy Way - Recommended!)

### Using GitHub Codespaces

**This is the easiest way to get started - no installation needed!**

1. Click the green **"Code"** button at the top of this page
2. Click on the **"Codespaces"** tab
3. Click **"Create codespace on main"**
4. Wait about 1-2 minutes while your coding environment sets up
5. You're ready to code! Everything is installed automatically.

**That's it!** Your environment is ready. All the tools you need are already installed.

---

## 🎮 How to Play the Game

Once your Codespace is ready (or if you're working locally):

1. Open the terminal at the bottom of the screen
2. Type:
   ```bash
   python main.py
   ```
3. Press Enter
4. Follow the on-screen instructions to play!

### Game Commands

- **north, south, east, west** (or n, s, e, w) - Move in that direction
- **look** - Examine your current location
- **help** - Show available commands
- **quit** - Exit the game

### Current Features

The base game includes:

- ✅ 3 connected rooms to explore (dungeon, hallway, courtyard)
- ✅ Movement system
- ✅ Win condition (escape the castle!)
- ✅ Simple command interface

**More features coming soon as we build them together in class!**

---

## 📚 For Teachers

This repository contains materials for a classroom exercise in AI-assisted Python programming.

### Included Materials

- **`castle_escape.py`** - The base game code (well-commented for beginners)
- **`student_handout.md`** - Printable handout for students
- **Lesson plans** - Structured session plans for teaching

### Teaching Approach

This project uses **Option A: "Feature Request Workshop"**:

1. Start with the minimal working game
2. Students suggest features
3. Use AI together to implement features
4. Discuss and understand the generated code
5. Test and debug as a class

### Learning Objectives

- **AI Literacy**: Understand AI as a collaborative tool
- **Code Comprehension**: Read and explain Python code
- **Critical Thinking**: Evaluate AI-generated code
- **Prompt Engineering**: Ask clear, specific questions
- **Iterative Development**: Build software feature-by-feature
- **Debugging Mindset**: Identify and fix issues

---

## 📁 Project Structure

```
adventure-game/
├── castle_escape.py         # Main game file - the base adventure
├── student_handout.md       # Student reference guide
├── requirements.txt         # Python dependencies (if any)
└── README.md               # This file
```

---

## 🛠️ Development Workflow

### Adding Features with AI

This project demonstrates how to collaborate with AI to build software:

1. **Brainstorm**: What feature do we want?
2. **Prompt**: How do we ask AI for it clearly?
3. **Review**: What code did AI generate?
4. **Understand**: What does each part do?
5. **Test**: Does it work as expected?
6. **Debug**: Fix any issues that arise
7. **Repeat**: What's the next feature?

### Example Feature Additions

Students typically suggest:

- 🎒 **Inventory system** - Pick up and carry items
- 🔑 **Locked doors** - Require keys to progress
- ⚔️ **Combat system** - Battle enemies
- 🧩 **Puzzles** - Riddles and challenges to solve
- 👥 **NPCs** - Characters to interact with
- 💎 **Treasure** - Items to collect and score
- 🗺️ **More rooms** - Expand the castle

---

## 🧪 For Students: Suggesting Features

### How to Propose a Feature

When suggesting a feature, think about:

1. **What does it do?**

   - Describe the feature clearly
   - Example: "Add an inventory where players can pick up and carry items"

2. **Why is it cool?**

   - How does it make the game better?
   - Example: "Items let us create puzzles with keys, tools, and treasures"

3. **How might it work?**

- Think through the user experience
- Example: "Type 'take key' to pick up a key, 'inventory' to see what you're carrying"

### Feature Ideas to Get Started

- 🏰 More rooms to explore (library, throne room, tower)
- 🐉 Enemy encounters (guards, monsters)
- 🔮 Magic spells or special abilities
- 🎭 NPCs with dialogue options
- 📜 Quest system with objectives
- ❤️ Health and status tracking
- 🎨 ASCII art for rooms
- 💾 Save/load game progress
- 🎲 Random events and surprises
- 🏆 Multiple endings based on choices

---

## 💻 Working on Your Own Computer (Optional)

If you prefer to work locally instead of using Codespaces:

### Prerequisites

- Python 3.8 or higher installed ([python.org](https://www. python.org/downloads/))
- Git installed ([git-scm.com](https://git-scm.com/))

### Setup

1. **Clone this repository:**

   ```bash
   git clone https://github.com/scottluskraa/adventure-game.git
   cd adventure-game
   ```

2. **Run the game:**

```bash
python castle_escape.py
```

3. **Start playing!**

---

## 📖 Learning Resources

### Python Basics

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python](https://www.w3schools. com/python/)
- [Real Python Tutorials](https://realpython.com/)

### Text-Based Games

- [Interactive Fiction Archive](https://www.ifarchive.org/)
- [Inform 7](http://inform7.com/) - Advanced text game creation

### AI-Assisted Coding

- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

## 🤝 Contributing

This is a learning project! If you're a student:

- Suggest features in class
- Help test and find bugs
- Share your modifications

If you're a teacher:

- Fork this repo and adapt for your classroom
- Share improvements or lesson plans
- Report issues or suggestions

---

## 🎓 Pedagogical Notes

### Why This Approach Works

1. **Immediate Engagement**: Students see working code from day one
2. **Student Ownership**: THEY design the features
3. **AI as Scaffolding**: Reduces syntax barriers, focuses on concepts
4. **Iterative Learning**: Concepts build naturally through features
5. **Authentic Practice**: Mirrors real-world development workflows
6. **Critical Thinking**: Students evaluate and critique AI code

### Key Teaching Moments

- **When AI makes mistakes**: Debugging teaches more than perfect code
- **When features conflict**: Discussing integration teaches architecture
- **When code is confusing**: Reading comprehension is essential
- **When students get creative**: Enthusiasm drives deeper learning

---

## 🆘 Troubleshooting

### Game Won't Run

- **Error: `python: command not found`**
  - Python isn't installed. Use Codespaces or install Python locally
- **Error: `No such file or directory`**
  - Make sure you're in the right folder: `cd adventure-game`

### Gameplay Issues

- **Can't move in a direction**

  - Check the room description - it tells you valid exits
  - Try typing just the direction: `north` instead of `go north`

- **Commands not working**
  - Type `help` to see available commands
  - Make sure spelling is correct
  - Commands are case-insensitive

### Code Questions

- **Don't understand the code?**
  - Read the comments - they explain what each section does
  - Try changing small things and see what happens
  - Ask your teacher or classmates
  - Use AI to explain specific lines (great learning opportunity!)

---

## 📝 Changelog

### Version 1.0 (Base Game)

- ✅ Three-room castle layout
- ✅ Movement system (north, south, east, west)
- ✅ Basic command parser
- ✅ Win condition (escape to freedom)
- ✅ Help system

### Coming Soon (Features to Add in Class)

- ⏳ Inventory system
- ⏳ Locked doors and keys
- ⏳ Items to collect
- ⏳ More rooms
- ⏳ Your ideas!

---

## 📄 License

This project is designed for educational use. Feel free to use, modify, and share for learning purposes.

---

## 🌟 Acknowledgments

- Created as a teaching tool for Python programming
- Designed to demonstrate AI-assisted development
- Built collaboratively with students and AI

---

## 💬 Questions or Ideas?

- **Students**: Share your feature ideas in class!
- **Teachers**: Open an issue or discussion on GitHub
- **Everyone**: Remember - learning to code is a journey. Enjoy the adventure! 🚀

---

**Happy Coding! May your castle escape be legendary!** 🏰✨
