from sudoku import Sudoku


sudoku = Sudoku()

sudoku.generate("hard")

print("Generated Sudoku:")
sudoku.draw()

solution = sudoku.copy()
solution.solve()

print("\nSolution:")
solution.draw()