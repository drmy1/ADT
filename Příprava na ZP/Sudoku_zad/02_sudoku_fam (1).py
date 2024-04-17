import numpy as np
import random
from sys import argv
import os


# Následující program obsahuje kostru řešení klasického sudoku.
# Vaším úkolem je upravit a doplnit program tak, aby řešil rodinu modifikovaných sudoku, kterou máte k dispozici ke stažení.
# Vám zadaná rodina může mít jiný počet řádků, sloupců a jiný tvar bloku než známe ze standardního sudoku.
# Pokud v souboru s daty není napsáno jinak, pravidla pro vyřešení jsou stejná (čísla se nesmí opakovat v řádku, sloupci, bloku)
# Implementujte načtení vaší rodiny sudoku ze souboru a upravte program tak, aby uměl vám zadanou rodinu sudoku řešit.
# Rodina Sudoku má vždy stejný tvar tedy:
#   stejný počet řádek
#   stejný počet sloupců
#   rozměr a poloha bloků zůstane vždy stejná
# Rodina Sudoku má vždy stejná pravidla.

# Hodnocení:
# Za správný load ze souboru [+5]
# Za správně ověřovaný řádek [+1]
# Za správně ověřovaný sloupec [+1]
# Za správně ověřovaný blok [+3]
# Za správně ověřovanou pozici [+3]
# Za správně vyřešené sudoku [+5]
# Za dodržení rozhraní main [+2]


EMPTY_VALUE = 0


class SudokuSolver:

    # neupravujte signaturu konstruktoru, tělo konstruktoru doplňte podle vaší potřeby
    def __init__(self, *args, **kwargs):
        #  !! neupravujte jméno proměnné (self.sudoku) bude použito pro automatickou kontrolu. Rozměr pole samozřejmě upravit můžete.

        self.sudoku = np.zeros([6, 6], dtype=int)

    def check_sequence(self, sequence: np.ndarray):

        arr = sequence

        return len(np.unique(arr[arr != 0])) == len(arr[arr != 0])

    def load(self, filepath: str) -> None:
        """
        Metoda načte sudoku ze souboru a uloží jej do proměnné self.sudoku.
        args:
            filepath: cesta k souboru se sudoku. Pro přesný formát souboru viz přiložené soubory.
        """
        # // todo implementujte načítání ze souboru. Viz přiložené soubory.

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

    def check_one_cell(self, row_index: int, column_index: int) -> bool:
        """
        Metoda zkontroluje, zda je konkrétní pozice na souřadnici v self.sudoku v souladu s pravidly.
        args:
            row_index: index řádku
            column_index: index sloupce
        return:
            bool: True, pokud je pozice v souladu s pravidly, jinak False
        """
        # // TODO implementujte kontrolu konkrétní souřadnice v sudoku

        return self.check_row(row_index) and \
            self.check_column(column_index) and \
            self.check_block(row_index, column_index)

    def check_row(self, r_index: int) -> bool:
        """
        Metoda zkontroluje, zda je řádek v self.sudoku v souladu s pravidly.
        args:
            r_index: index řádku
        return:
            bool: True, pokud je řádek v souladu s pravidly, jinak False
        """
        # // TODO implementujte kontrolu řádku
        return self.check_sequence(self.sudoku[r_index, :])

    def check_column(self, c_index: int) -> bool:
        """
        Metoda zkontroluje, zda je sloupec v self.sudoku v souladu s pravidly.
        args:
            c_index: index sloupce
        return:
            bool: True, pokud je sloupec v souladu s pravidly, jinak False
        """
        # // TODO implementujte kontrolu sloupce
        return self.check_sequence(self.sudoku[:, c_index])

    def check_block(self, number_row_position: int, number_col_position: int) -> bool:
        """
        Metoda zkontroluje, zda je blok v self.sudoku v souladu s pravidly. Každý blok je jednoznačně určen kterýmkoli prvkem, který v něm leží.
        V klasickém sudoku, kde jsou bloky v rozměru 3x3 tedy všechny kombinace (0,0), (1,2), ..., (2,2). vede na stejný blok.

        args:
            number_row_position: index řádku konkrétního čísla v sudoku
            number_col_position: index sloupce konkrétního čísla v sudoku
        return:
            bool: True, pokud je blok, ve kterém leží souřadnice na vstupu, v souladu s pravidly, jinak False
        """
        # print(self.sudoku[number_row_position - number_row_position %
        #      3: number_row_position - number_row_position % 3 + 2])
        # print(self.sudoku[number_col_position - number_col_position %
        #       2: number_col_position - number_col_position % 2 + 3])
        # // TODO implementujte kontrolu bloku nezapomeňte, že vám přidělená rodina sudoku může mít jiný tvar bloku.
        row_start = (number_row_position // 3) * 2
        column_start = (number_col_position // 3) * 3

        block = self.sudoku[row_start: row_start +
                            2, column_start: column_start + 3]
        return self.check_sequence(block.reshape(-1))

    def solve(self) -> bool:
        """
        Metoda vyřeší sudoku. Tj. upraví pole self.sudoku tak, aby bylo vyřešené.
        return:
            bool: True, pokud se sudoku podařilo vyřešit, jinak False
        """

        # // TODO implementujte řešení sudoku
        for r in range(6):
            for c in range(6):
                # skip filled cells
                if self.sudoku[r, c] != EMPTY_VALUE:
                    continue

                # fill empty cell with some value
                possible_values = list(range(1, 7))
                random.shuffle(possible_values)
                for value in possible_values:
                    self.sudoku[r, c] = value

                    # check if the number fits the cell
                    if not self.check_one_cell(r, c):
                        continue

                    # try to solve another cell (recursion)
                    if self.solve():
                        return True

                # no number fits the cell (the `return True` statement was not reached) -> backtrack
                self.sudoku[r, c] = EMPTY_VALUE
                return False

        # all cells are filled -- the sudoku is solved!
        return True

    def check_field(self) -> bool:
        """
        Metoda zkontroluje, zda je celé pole self.sudoku v souladu s pravidly.
        return:
            bool: True, pokud je celé pole v souladu s pravidly, jinak False
        """
        # // TODO implementujte kontrolu celého pole
        for i in range(6):
            for j in range(6):
                if not self.check_one_cell(i, j):
                    return False
        return True


def main(filepath: str) -> np.ndarray:
    """
    Hlavní funkce programu. Zde načtěte sudoku ze souboru a vyřešte jej.

    args:
        filepath: cesta k souboru se sudoku. Pro přesný formát souboru viz přiložené soubory.
    return:
        np.ndarray: vyřešené sudoku
    """
    sudoku_solver = SudokuSolver()

    if os.path.exists(filepath):
        # // TODO načtete sudoku z filepath  pomocí metody load(self, filepath:str)
        sudoku_solver.load(filepath)
        # // TODO sudoku vyřešte pomocí volání metody def solve(self)

        print(sudoku_solver.solve())
        print(sudoku_solver.sudoku)

        return sudoku_solver.sudoku  # vyřešené pole pro automatickou kontrolu

    raise Exception


if __name__ == "__main__":
    # Program přijímá cestu k souboru. Bude spouštěn následujícím příkazem "python main.py some/path_to/sudoku.txt"
    #  // todo implementujte zpracování argumentu z příkazové řádky.

    if len(argv) != 2:
        print("Neplatný počet argumentů. Zadejte cestu k souboru se sudoku.")
        exit(1)

    sudoku_filepath = argv[1]

    main(sudoku_filepath)
