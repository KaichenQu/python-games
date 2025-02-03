# All Games

This repository contains multiple games implemented using Python and Pygame. The games included are Snake, Yahtzee, Gomoku, and Sokoban. Each game can be launched from a unified interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Games](#games)
  - [Snake](#snake)
  - [Yahtzee](#yahtzee)
  - [Gomoku](#gomoku)
  - [Sokoban](#sokoban)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/all-games.git
   cd all-games
   ```

2. Install the required dependencies:
   ```sh
   pip install pygame
   ```

## Usage

To start the game launcher, run the following command:

```sh
python display.py
```

or

```sh
python3 display.py
```

## Games

### Snake

The classic Snake game where the player controls a snake to eat food and grow longer. The game ends if the snake collides with the walls or itself.

- **File:** `main.py`
- **Controls:**
  - Arrow keys to change direction
  - ESC to quit

### Yahtzee

A dice game where players roll dice to achieve specific combinations and score points.

- **File:** `Run.py`
- **Controls:**
  - Mouse to interact with the UI elements

### Gomoku

A strategy board game where players take turns placing stones on a 15x15 board, aiming to get five in a row.

- **File:** `main.py`
- **Controls:**
  - Mouse to place chess

### Sokoban

A puzzle game where the player pushes boxes to designated locations in a warehouse.

- **File:** `game.py`
- **Controls:**
  - Arrow keys to move
  - R to retry the level
  - Space to proceed to the next level after winning
  - ESC to quit

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
