from random import randint, sample
from typing import Literal


def drawGrid(grid: list) -> None:
    for row in range(9):
        print(grid[row])


def findEmptyCell(grid: list) -> tuple[int, int] | Literal[False]:
    for i in range(81):
        row = i // 9
        col = i % 9

        if grid[row][col] == 0:
            return row, col

    return False


def checkRow(grid: list, num: int, row: int) -> bool:
    return not num in grid[row]


def checkColumn(grid: list, num: int, col: int) -> bool:
    return not num in (
        grid[0][col],
        grid[1][col],
        grid[2][col],
        grid[3][col],
        grid[4][col],
        grid[5][col],
        grid[6][col],
        grid[7][col],
        grid[8][col],
    )


def checkSquare(grid: list, num: int, row: int, col: int) -> bool:
    square = []

    if row < 3:
        if col < 3:
            square = [grid[i][0:3] for i in range(3)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(3)]
        else:
            square = [grid[i][6:9] for i in range(3)]
    elif row < 6:
        if col < 3:
            square = [grid[i][0:3] for i in range(3, 6)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(3, 6)]
        else:
            square = [grid[i][6:9] for i in range(3, 6)]
    else:
        if col < 3:
            square = [grid[i][0:3] for i in range(6, 9)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(6, 9)]
        else:
            square = [grid[i][6:9] for i in range(6, 9)]

    return not num in (square[0] + square[1] + square[2])


def isValid(grid: list, num: int, row: int, col: int) -> bool:
    return (
        checkRow(grid, num, row)
        and checkColumn(grid, num, col)
        and checkSquare(grid, num, row, col)
    )


def fillSudoku(grid: list) -> bool:
    empty_cell = findEmptyCell(grid)

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in sample(range(1, 10), 9):
        if isValid(grid, num, row, col):
            grid[row][col] = num

            if fillSudoku(grid):
                return True

            grid[row][col] = 0

    return False


def countSolutions(grid: list) -> int:
    empty_cell = findEmptyCell(grid)

    if not empty_cell:
        return 1

    row, col = empty_cell
    count = 0

    for num in range(1, 10):
        if isValid(grid, num, row, col):
            grid[row][col] = num

            count += countSolutions(grid)

            grid[row][col] = 0

            if count > 1:
                return count

    return count


grid = [[0 for _ in range(9)] for _ in range(9)]

fillSudoku(grid)

print("Generated Sudoku:")
drawGrid(grid)

attempts = 20

while attempts > 0:
    row = randint(0, 8)
    col = randint(0, 8)

    if grid[row][col] == 0:
        continue

    backup = grid[row][col]
    grid[row][col] = 0

    copyGrid = [row[:] for row in grid]

    solutions = countSolutions(copyGrid)

    if solutions != 1:
        # Removing this number made the puzzle invalid
        # (0 solutions or multiple solutions)
        grid[row][col] = backup

    attempts -= 1

print("\nFinal puzzle:")
drawGrid(grid)
