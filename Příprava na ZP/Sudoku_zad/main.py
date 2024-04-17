import random
import numpy as np

EMPTY_VALUE = 0


class SudokuSolver:

    def __init__(self, field: np.ndarray | None = None, n_rows: int = 9, n_columns: int = 9):

        if field is None:
            field = np.zeros([n_rows, n_columns], dtype=int)
        self.field = field
        self.n_rows = n_rows
        self.n_columns = n_columns

    def check_sequence(self, sequence: np.ndarray):

        arr = sequence

        return len(np.unique(arr[arr != 0])) == len(arr[arr != 0])

    def check_one_cell(self, row_index: int, column_index: int):

        return self.check_row(row_index) and \
            self.check_column(column_index) and \
            self.check_block(row_index, column_index)

    def check_row(self, row_index: int):

        return self.check_sequence(self.field[row_index, :])

    def check_column(self, column_index: int):

        return self.check_sequence(self.field[:, column_index])

    def check_block(self, row_index: int, column_index: int):
        return self.check_sequence(self.field[row_index - row_index % 3:row_index - row_index % 3 + 3,
                                              column_index - column_index % 3:column_index - column_index % 3 + 3])

    def solve(self):
        for r in range(self.n_rows):
            for c in range(self.n_columns):
                # skip filled cells
                if self.field[r, c] != EMPTY_VALUE:
                    continue

                # fill empty cell with some value
                possible_values = list(range(1, 10))
                random.shuffle(possible_values)
                for value in possible_values:
                    self.field[r, c] = value

                    # check if the number fits the cell
                    if not self.check_one_cell(r, c):
                        continue

                    # try to solve another cell (recursion)
                    if self.solve():
                        return True

                # no number fits the cell (the `return True` statement was not reached) -> backtrack
                self.field[r, c] = EMPTY_VALUE
                return False

        # all cells are filled -- the sudoku is solved!
        return True

    """        
    if self.check_sequence(self.field[:, :]):
            return True
        else:
            for fields in self.field:
                for i in range(9):
                    if fields[i] == EMPTY_VALUE:
                        for j in range(1, 10):
                            if self.check_one_cell(i, j):
                                fields[i] = j
                                if self.solve():
                                    return True
                                else:
                                    fields[i] = EMPTY_VALUE
                        return False
            return True"""

    def check_field(self):
        for i in range(9):
            for j in range(9):
                if not self.check_one_cell(i, j):
                    return False
        return True

    def load(self, path):
        with open(path, "r") as file:
            lines = file.readlines()
            numeric_line = [[int(v) for v in line.strip().split(";")]
                            for line in lines]
            self.field = np.array(numeric_line)


def main():
    sudoku_solver = SudokuSolver()
    sudoku_solver.load("removed_10.csv")

    print(sudoku_solver.solve())
    print(sudoku_solver.field)


if __name__ == "__main__":
    main()
