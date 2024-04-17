import numpy as np
import re


class SudokuSolver:
    def __init__(self):
        self.sudoku = np.zeros((6, 6), dtype=int)

    def load(self, filepath):
        with open(filepath, "r", encoding="utf8") as f:
            line_index = 0
            for line in f:
                if line.startswith("=") or line.startswith("-"):
                    continue
                else:
                    symbol_index = 0
                    for symbol in line:
                        match symbol:
                            case " " | "|":
                                continue
                            case "?":
                                symbol = 0
                                # print(symbol)
                                # print(line_index, symbol_index)
                                self.sudoku[line_index,
                                            symbol_index] = int(symbol)
                                symbol_index += 1
                            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                                # print(symbol)
                                # print(line_index, symbol_index)
                                self.sudoku[line_index,
                                            symbol_index] = int(symbol)
                                symbol_index += 1
                line_index += 1

    def is_valid_cell(self, row, col, num):
        for i in range(6):
            if self.sudoku[i, col] == num:
                return False
        for j in range(6):
            if self.sudoku[row, j] == num:
                return False
        block_row_start = (row // 3) * 3
        block_col_start = (col // 3) * 3
        for i in range(block_row_start, block_row_start + 3):
            for j in range(block_col_start, block_col_start + 3):
                if self.sudoku[i, j] == num:
                    return False
        return True

    def is_valid_row(self, row):
        for i in range(6):
            if not self.is_valid_cell(row, i, self.sudoku[row, i]):
                return False
        return True

    def is_valid_column(self, col):
        for i in range(6):
            if not self.is_valid_cell(i, col, self.sudoku[i, col]):
                return False
        return True

    def is_valid_block(self, row, col):
        block_row_start = (row // 3) * 3
        block_col_start = (col // 3) * 3
        for i in range(block_row_start, block_row_start + 3):
            for j in range(block_col_start, block_col_start + 3):
                if not self.is_valid_cell(i, j, self.sudoku[i, j]):
                    return False
        return True

    def solve(self):
        for i in range(6):
            for j in range(6):
                if self.sudoku[i, j] == 0:
                    for num in range(1, 7):
                        if self.is_valid_cell(i, j, num):
                            self.sudoku[i, j] = num
                            if self.solve():
                                return True
                            self.sudoku[i, j] = 0
                    return False
        return True


def main(filepath):
    solver = SudokuSolver()
    solver.load(filepath)
    solver.solve()
    print(solver.sudoku)


if __name__ == "__main__":
    filepath = "8_rm15_sol1.txt.txt"
    main(filepath)
