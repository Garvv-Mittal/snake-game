# 🐍 Snake Game (Python Turtle)

A classic **Snake Game** built using **Python** and the **Turtle graphics module**.  
The game includes movement controls, food generation, score tracking, wall collision, and self-collision detection.

---

## ✨ Features

- 🎮 Smooth snake movement using keyboard controls
- 🍎 Random food generation
- 📊 Live score tracking
- 🔄 Automatic reset on collision
- 🧠 Modular code using classes
- ⚡ Optimized animation using `screen.tracer(0)`

---

## 🛠️ Tech Stack

- **Python 3**
- **Turtle module**
- **Time module**

---

## 📁 File Structure

```text
Snake-Game/
├── main.py
│   ├─ Game loop and screen setup
│   ├─ Keyboard controls
│   ├─ Collision detection
│   └─ Game state management
│
├── snake.py
│   ├─ Snake class
│   ├─ Snake movement logic
│   ├─ Extend and reset functionality
│
├── food.py
│   ├─ Food class
│   ├─ Random food positioning
│
├── scoreboard.py
│   ├─ Score display
│   ├─ Score increment
│   └─ Reset mechanism
│
└── README.md
    └─ Project documentation