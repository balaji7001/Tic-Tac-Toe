# 🤖Smart Tic-Tac-Toe


A classic Tic-Tac-Toe game with a clean graphical user interface (GUI) built using Python's tkinter library. This project features two game modes: Player vs. Player and Player vs. a highly intelligent Computer opponent. The AI uses the minimax algorithm to play optimally, ensuring a challenging experience.

# ✨ Features

Two Game Modes:
```bash 
https://tik-tat-toe.netlify.app/
```
Player vs. Player (PvP): Play against a friend on the same computer.

Player vs. Computer (PvC): Test your skills against an intelligent AI that never makes a mistake.

Intuitive GUI: A simple and clean 3x3 grid interface.

Optimal AI: The computer player uses the minimax algorithm to make the best possible move in every situation, guaranteeing a challenging match.

Status Updates: The game provides real-time updates on whose turn it is, who won, or if the game is a draw.

# 📦 Packages Used
This project is built using only Python's standard library, so no external packages need to be installed. The necessary modules are included with any standard Python 3.x installation.

tkinter: Python's standard GUI library for creating the game window and board.

random: Used for basic functionalities like choosing the first move in some scenarios.

🛠️ Installation
Ensure Python is installed: You need to have Python 3.x installed on your system. You can download it from python.org.

Clone the repository:

```bash
python --version
```

### Installation

1.  **Clone the repository**
    Open your terminal and clone the repository using this command:
    ```bash
    git clone https://github.com/balaji7001/Tic-Tac-Toe.git
    ```

2.  **Navigate to the project directory**
    Change into the newly cloned folder:
    ```bash
    cd Tic-Tac-Toe
    ```

---

## 🚀 Usage

To run the game, simply execute the Python script from your terminal:

```bash
python tic_tac_toe.py
```

The game will start, and you will be prompted to make your move. Enjoy trying to force a draw against the AI!

---
The game window will appear, allowing you to choose your game mode and start playing.
Opens in a new window


<img width="350" height="400" alt="image" src="https://github.com/user-attachments/assets/eeab1cd2-cfc7-4386-a1bd-4963ba99a49e" />



# 🧠 The AI Explained (Minimax Algorithm)


The AI in the Player vs. Computer mode is powered by the minimax algorithm. This is a recursive algorithm for choosing an optimal move for a player in a two-player game. It works by:

Exploring possibilities: It simulates every possible move from the current board state.

Assigning scores: It assigns a score to each final game state (win, loss, or draw). A win for the AI gets a high positive score, a loss gets a high negative score, and a draw gets a score of zero.

Maximizing and minimizing: The AI chooses the move that leads to the highest possible score, while assuming that the human player (the "minimizing" player) will always choose the move that leads to the lowest score for the AI.

This process allows the AI to "look ahead" and select a move that guarantees a win if one is available, or at least prevents the opponent from winning
