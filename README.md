# Maze Puzzle Project

![Maze Puzzle](https://example.com/your-image-link) <!-- Tambahkan tautan gambar yang sesuai -->

## Overview

Welcome to the Maze Puzzle Project! This project is a culmination of my final project for the Algorithm Strategy course. The goal is to generate random mazes of varying sizes and solve them using the A* search algorithm. The application also includes a graphical user interface (GUI) using Tkinter to visualize the maze and the solving process.

## Features

- **Maze Generation:** Generates mazes of different sizes (11x11, 15x15, 21x21, 25x25).
- **A* Search Algorithm:** Efficiently finds the shortest path from the start to the goal.
- **Visualization:** Visualizes the maze and the solving process step-by-step.
- **Interactive GUI:** Allows users to select levels, reset the maze, solve the maze, and view statistics like solving time.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python)
- Additional libraries: `heapq`, `time`

### Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/yourusername/maze-puzzle.git
    cd maze-puzzle
    ```

2. **Install Required Libraries:**

    No additional libraries need to be installed as `heapq` and `time` are part of Python's standard library. Ensure that Tkinter is installed with your Python distribution.

### Running the Application

1. **Generate Mazes:**

    Ensure `generate_maze.py` and `generate_and_export.py` are correctly set up to generate and export mazes.

2. **Run the Main Application:**

    ```sh
    python main.py
    ```

3. **Interactive GUI:**

    - Select the maze level from the right-hand panel.
    - Click "Generate Maze" to create a new maze.
    - Click "Solve Maze" to start the A* solving process.
    - View the solving process and final path in the canvas and text areas.

## Project Structure

```plaintext
Maze_puzzle/
├── generate_maze.py        # Maze generation logic
├── generate_and_export.py  # Maze export functionality
├── astar.py                # A* search algorithm implementation
├── visualize_maze.py       # Visualization functions (if separate from main.py)
└── main.py                 # Main application with GUI
