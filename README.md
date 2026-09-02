# Sudoku

A Python implementation of a Sudoku solver and generator.

This project was developed to explore algorithmic problem solving and the logic behind generating and solving Sudoku puzzles. It provides two main functionalities: solving existing Sudoku boards and generating new puzzles from scratch.

## Features

* 🧩 **Sudoku Solver** — Solves valid Sudoku puzzles automatically.
* 🎲 **Sudoku Generator** — Generates new Sudoku puzzles programmatically.
* 🧠 **Algorithmic solving** — Uses backtracking and constraint-based logic to find solutions.
* ✅ **Puzzle validation** — Checks whether numbers can be placed without violating Sudoku rules.
* 🧪 **Tests** — Includes automated tests for the core functionality.
* 🐍 **Pure Python** — Built entirely with Python.

## How It Works

### Solver

The solver receives a Sudoku board and searches for a valid solution by identifying empty cells and trying possible values.

When a value leads to an invalid state, the algorithm backtracks to the previous decision and tries another possibility. This allows the solver to systematically explore the possible solutions until the puzzle is completed.

### Generator

The generator works in the opposite direction: instead of solving an existing puzzle, it creates a new valid Sudoku board.

It first builds a valid completed board and then removes values while maintaining the validity of the puzzle. This produces a playable Sudoku that can subsequently be solved by the solver.

## Project Structure

```text
Sudoku/
├── src/
│   └── sudoku/
│       └── ...
├── tests/
│   └── ...
├── pyproject.toml
├── uv.lock
└── README.md
```

## Requirements

* Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/janpeix04/Sudoku.git
cd Sudoku
```

Install the project dependencies:

```bash
uv sync
```

Alternatively, if you are using a standard Python environment:

```bash
pip install -e .
```

## Usage

The project provides functionality for both generating and solving Sudoku puzzles.

Example workflow:

```python
# Generate a new Sudoku
puzzle = generate_sudoku()

# Solve the generated puzzle
solution = solve_sudoku(puzzle)
```

> The exact API may vary depending on the implementation in the `src/sudoku` package.

## Testing

Run the test suite with:

```bash
pytest
```

## Technologies

* **Python**
* **Pytest**
* **uv**

## Purpose

This project was created as a practical exercise in algorithm design, recursion, backtracking, constraint solving, and software testing.

## Author

**Jan Peix**

[GitHub](https://github.com/janpeix04)
