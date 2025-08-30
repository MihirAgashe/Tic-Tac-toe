### Tic-Tac-Toe Game with Python's Turtle Library 🕹️

This is a simple implementation of the classic Tic-Tac-Toe game created using the **Turtle** graphics library in Python. It's a fun and interactive way to showcase basic object-oriented programming (OOP) principles and event handling in Python.

---

### Features ✨

* **Interactive Gameplay**: Players can click on the squares to place their 'X' or 'O'.
* **Visual Feedback**: The game board is dynamically updated with 'X's (in red) and 'O's (in blue) as players take their turns.
* **Win/Draw Detection**: The game automatically checks for winning combinations (rows, columns, and diagonals) and declares a winner or a draw.
* **Simple OOP Design**: The game uses a `GridTurtle` class to represent each square on the board, encapsulating its state and behavior.

---

### How to Play 🎮

1. **Run the Script**: Simply execute the `main.py` file.
2. **Take Turns**: Player 'X' goes first, followed by player 'O'.
3. **Click to Play**: Click on any empty square on the board to place your symbol.
4. **Game Over**: The game ends when a player gets three of their symbols in a row or when all squares are filled, resulting in a draw. The console will display the outcome.

---

### Project Structure 📂

* `main.py`: Contains all the game logic, including the `GridTurtle` class, game state management, and the functions for checking game conditions.

---

### Dependencies 📦

This project uses the built-in **Turtle** library, so no additional installations are required.

To run the game, you only need a standard Python 3 environment.

---

### Code Highlights 🔍

The core of the game is the `GridTurtle` class, which inherits from `turtle.Turtle`. Each instance of this class represents a single square on the Tic-Tac-Toe grid.

* `__init__`: Initializes the turtle's shape, size, and position on the screen.
* `handle_click`: This method is triggered when a user clicks on a square. It checks if the square is already used, updates the game state, and draws the 'X' or 'O' symbol on the screen. It also calls the win-checking functions.

The game uses global variables within the class (`GridTurtle.turn`, `GridTurtle.count`, `GridTurtle.end_game`) to manage the shared state of the game, such as whose turn it is and whether the game has ended.

---

### Future Improvements 🚀

* **User Interface**: Add on-screen text to display the current turn and the game's outcome instead of just printing to the console.
* **Single-Player Mode**: Implement an AI opponent to play against.
* **Replay Option**: Add a button to reset the game and play again without restarting the script.