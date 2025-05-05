# 4x4 Grid Game

4×4华容道小游戏

This project is a simple 4x4 grid game implemented in Python. The game allows players to interact with a grid, making moves and checking for win conditions.

## Project Structure

```
4x4-grid-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── game
│   │   ├── __init__.py  # Marks the game directory as a package
│   │   ├── grid.py      # Contains the Grid class for the game grid
│   │   └── logic.py     # Contains the GameLogic class for game mechanics
│   └── utils
│       ├── __init__.py  # Marks the utils directory as a package
│       └── helpers.py    # Contains helper functions for the game
├── tests
│   ├── test_grid.py     # Unit tests for the Grid class
│   └── test_logic.py    # Unit tests for the GameLogic class
├── requirements.txt      # Required Python libraries
└── README.md             # Project documentation
```

## Installation

To install the required libraries, run:

```
pip install -r requirements.txt
```

## Usage

To start the game, run the following command:

```
python src/main.py
```
