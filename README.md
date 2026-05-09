# Tic-Tac-Toe (Python Terminal)

A classic, interactive Tic-Tac-Toe game designed to run directly in your terminal. This implementation features a clean board rendering, input validation, and automated win/draw detection.

## Features

- **Dynamic Rendering:** The terminal clears after every move to keep the interface clean and focused.
- **Marker Selection:** Player 1 can choose to be 'X' or 'O', and the game automatically assigns the remaining marker to Player 2.
- **Input Validation:** Prevents players from choosing occupied spaces, entering non-numeric characters, or using coordinates outside the 1–9 range.
- **Automated Logic:** Comprehensive status checking for horizontal, vertical, and diagonal wins, as well as draw detection.

## How to Play

1. **Start the Game:** Run the script using Python.
2. **Choose Markers:** Player 1 selects 'X' or 'O' when prompted.
3. **Make Your Move:** Players enter a number from **1 to 9** to place their marker on the board.

### Input Mapping
The board positions are mapped to the grid as follows:

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
| 7 | 8 | 9 |

## 💻 Installation & Usage

1. **Ensure Python is installed:** Check your version with `python --version`.
2. **Save the code:** Save your script as `tic_tac_toe.py`.
3. **Run the game:**
   python tic_tac_toe.py