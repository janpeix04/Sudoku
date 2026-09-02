from typing import Literal

grid = []
grid.append([5, 3, 0, 0, 7, 0, 0, 0, 0])
grid.append([6, 0, 0, 1, 9, 5, 0, 0, 0])
grid.append([0, 9, 8, 0, 0, 0, 0, 6, 0])
grid.append([8, 0, 0, 0, 6, 0, 0, 0, 3])
grid.append([4, 0, 0, 8, 0, 3, 0, 0, 1])
grid.append([7, 0, 0, 0, 2, 0, 0, 0, 6])
grid.append([0, 6, 0, 0, 0, 0, 2, 8, 0])
grid.append([0, 0, 0, 4, 1, 9, 0, 0, 5])
grid.append([0, 0, 0, 0, 8, 0, 0, 7, 9])


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


def solveSudoku(grid: list):
    empty_cell = findEmptyCell(grid)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if isValid(grid, num, row, col):
            grid[row][col] = num

            if solveSudoku(grid):
                return True

            grid[row][col] = 0
    return False


drawGrid(grid)
solveSudoku(grid)
print("\n")
drawGrid(grid)
