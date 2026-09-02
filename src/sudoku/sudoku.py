from random import randint, sample


class Sudoku:
    DIFFICULTIES = {  # noqa: RUF012
        "easy": 40,
        "medium": 36,
        "hard": 26,
    }

    def __init__(self) -> None:
        self.grid = self._empty_grid()

    @staticmethod
    def _empty_grid() -> list[list[int]]:
        return [[0 for _ in range(9)] for _ in range(9)]

    def reset(self) -> None:
        self.grid = self._empty_grid()

    def copy(self) -> Sudoku:
        new_sudoku = Sudoku()
        new_sudoku.grid = [row[:] for row in self.grid]
        return new_sudoku

    def draw(self) -> None:
        for row in self.grid:
            print(row)

    def solve(self) -> bool:
        empty_cell = self._find_empty_cell(self.grid)

        if empty_cell is None:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if self._is_valid(self.grid, num, row, col):
                self.grid[row][col] = num

                if self.solve():
                    return True

                self.grid[row][col] = 0

        return False

    def fill(self) -> bool:
        empty_cell = self._find_empty_cell(self.grid)

        if empty_cell is None:
            return True

        row, col = empty_cell

        for num in sample(range(1, 10), 9):
            if self._is_valid(self.grid, num, row, col):
                self.grid[row][col] = num
                if self.fill():
                    return True

                self.grid[row][col] = 0

        return False

    def count_solutions(self) -> int:
        return self._count_solutions(self.grid)

    def _count_solutions(self, grid: list[list[int]]) -> int:
        empty_cell = self._find_empty_cell(grid)

        if empty_cell is None:
            return 1

        row, col = empty_cell
        count = 0

        for num in range(1, 10):
            if self._is_valid(grid, num, row, col):
                grid[row][col] = num

                count += self._count_solutions(grid)

                grid[row][col] = 0

                if count > 1:
                    return count

        return count

    def generate(self, difficulty: str = "easy") -> None:
        if difficulty not in self.DIFFICULTIES:
            raise ValueError(
                f"Unknown difficulty: {difficulty}. "
                f"Choose from {list(self.DIFFICULTIES.keys())}"
            )

        self.reset()
        self.fill()

        target_clues = self.DIFFICULTIES[difficulty]
        clues = 81

        while clues > target_clues:
            row = randint(0, 8)
            col = randint(0, 8)

            if self.grid[row][col] == 0:
                continue

            backup = self.grid[row][col]
            self.grid[row][col] = 0
            test_grid = [row[:] for row in self.grid]
            solutions = self._count_solutions(test_grid)

            if solutions == 1:
                clues -= 1
            else:
                self.grid[row][col] = backup

    @staticmethod
    def _find_empty_cell(
        grid: list[list[int]],
    ) -> tuple[int, int] | None:
        for i in range(81):
            row = i // 9
            col = i % 9

            if grid[row][col] == 0:
                return row, col

        return None

    @staticmethod
    def _check_row(
        grid: list[list[int]],
        num: int,
        row: int,
    ) -> bool:
        return num not in grid[row]

    @staticmethod
    def _check_column(
        grid: list[list[int]],
        num: int,
        col: int,
    ) -> bool:
        for row in range(9):
            if grid[row][col] == num:
                return False

        return True

    @staticmethod
    def _check_square(
        grid: list[list[int]],
        num: int,
        row: int,
        col: int,
    ) -> bool:
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if grid[r][c] == num:
                    return False

        return True

    @classmethod
    def _is_valid(
        cls,
        grid: list[list[int]],
        num: int,
        row: int,
        col: int,
    ) -> bool:
        return (
            cls._check_row(grid, num, row)
            and cls._check_column(grid, num, col)
            and cls._check_square(grid, num, row, col)
        )
