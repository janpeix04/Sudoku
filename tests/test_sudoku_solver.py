from sudoku.sudoku_solver import solveSudoku


def is_solved(grid):
    numbers = set(range(1, 10))

    # Check rows
    for row in grid:
        if set(row) != numbers:
            return False

    # Check columns
    for col in range(9):
        column = {grid[row][col] for row in range(9)}
        if column != numbers:
            return False

    # Check 3x3 squares
    for square_row in range(0, 9, 3):
        for square_col in range(0, 9, 3):
            square = {
                grid[row][col]
                for row in range(square_row, square_row + 3)
                for col in range(square_col, square_col + 3)
            }

            if square != numbers:
                return False

    return True


def test_easy_sudoku():
    grid = [
        [0, 0, 0, 1, 0, 0, 2, 0, 4],
        [0, 0, 7, 5, 8, 6, 9, 1, 3],
        [0, 1, 0, 3, 0, 0, 0, 0, 7],
        [0, 3, 0, 6, 5, 0, 4, 7, 9],
        [0, 0, 8, 7, 0, 3, 0, 6, 2],
        [0, 0, 0, 2, 0, 0, 5, 0, 8],
        [8, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 9, 0, 1, 0, 0, 2, 0],
        [2, 5, 0, 4, 0, 0, 8, 9, 0],
    ]

    solution = [
        [6, 8, 3, 1, 7, 9, 2, 5, 4],
        [4, 2, 7, 5, 8, 6, 9, 1, 3],
        [9, 1, 5, 3, 2, 4, 6, 8, 7],
        [1, 3, 2, 6, 5, 8, 4, 7, 9],
        [5, 9, 8, 7, 4, 3, 1, 6, 2],
        [7, 6, 4, 2, 9, 1, 5, 3, 8],
        [8, 7, 1, 9, 6, 2, 3, 4, 5],
        [3, 4, 9, 8, 1, 5, 7, 2, 6],
        [2, 5, 6, 4, 3, 7, 8, 9, 1],
    ]
    assert solveSudoku(grid) is True
    assert is_solved(grid)
    assert grid == solution


def test_medium_sudoku():
    grid = [
        [8, 2, 7, 0, 1, 5, 0, 4, 3],
        [3, 0, 1, 2, 4, 9, 0, 7, 6],
        [0, 0, 0, 8, 0, 0, 0, 2, 5],
        [6, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 1, 8, 3, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 1, 0, 3, 0],
        [0, 6, 2, 0, 0, 4, 3, 0, 0],
        [1, 0, 5, 0, 0, 0, 4, 8, 0],
        [0, 0, 0, 9, 0, 0, 0, 1, 0],
    ]

    solution = [
        [8, 2, 7, 6, 1, 5, 9, 4, 3],
        [3, 5, 1, 2, 4, 9, 8, 7, 6],
        [4, 9, 6, 8, 3, 7, 1, 2, 5],
        [6, 4, 3, 5, 7, 8, 2, 9, 1],
        [5, 1, 8, 3, 9, 2, 7, 6, 4],
        [2, 7, 9, 4, 6, 1, 5, 3, 8],
        [9, 6, 2, 1, 8, 4, 3, 5, 7],
        [1, 3, 5, 7, 2, 6, 4, 8, 9],
        [7, 8, 4, 9, 5, 3, 6, 1, 2],
    ]
    assert solveSudoku(grid) is True
    assert is_solved(grid)
    assert grid == solution


def test_hard_sudoku():
    grid = [
        [0, 0, 4, 0, 0, 0, 7, 0, 1],
        [0, 0, 0, 2, 0, 0, 5, 9, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 7, 8, 5, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 9, 3, 0, 0, 0, 0],
        [0, 4, 0, 7, 0, 9, 6, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 2, 0, 6, 1, 0, 0, 0, 9],
    ]

    solution = [
        [2, 9, 4, 3, 8, 5, 7, 6, 1],
        [1, 3, 6, 2, 7, 4, 5, 9, 8],
        [7, 5, 8, 1, 9, 6, 3, 2, 4],
        [9, 1, 3, 4, 2, 7, 8, 5, 6],
        [4, 7, 2, 5, 6, 8, 9, 1, 3],
        [6, 8, 5, 9, 3, 1, 2, 4, 7],
        [8, 4, 1, 7, 5, 9, 6, 3, 2],
        [3, 6, 9, 8, 4, 2, 1, 7, 5],
        [5, 2, 7, 6, 1, 3, 4, 8, 9],
    ]
    assert solveSudoku(grid) is True
    assert is_solved(grid)
    assert grid == solution


def test_expert_sudoku():
    grid = [
        [9, 0, 3, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 6],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 6, 0, 7],
        [1, 0, 0, 7, 3, 0, 0, 8, 0],
        [0, 0, 0, 0, 8, 5, 0, 0, 1],
        [3, 0, 5, 0, 0, 0, 0, 1, 0],
        [7, 0, 6, 0, 0, 0, 4, 0, 0],
        [8, 0, 0, 4, 7, 3, 5, 6, 2],
    ]

    solution = [
        [9, 1, 3, 5, 6, 8, 2, 7, 4],
        [2, 5, 4, 1, 9, 7, 8, 3, 6],
        [6, 8, 7, 3, 4, 2, 1, 5, 9],
        [5, 3, 8, 2, 1, 9, 6, 4, 7],
        [1, 6, 2, 7, 3, 4, 9, 8, 5],
        [4, 7, 9, 6, 8, 5, 3, 2, 1],
        [3, 4, 5, 9, 2, 6, 7, 1, 8],
        [7, 2, 6, 8, 5, 1, 4, 9, 3],
        [8, 9, 1, 4, 7, 3, 5, 6, 2],
    ]
    assert solveSudoku(grid) is True
    assert is_solved(grid)
    assert grid == solution
