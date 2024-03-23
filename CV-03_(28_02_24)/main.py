from dataclasses import dataclass
import random
import timeit
from typing import Callable
import plotly.express as px

COLLECTION_SIZE = 100000
N_TESTS = 1000  # Number of test runs


@dataclass
class Rectangle:
    a: int
    b: int

    def __eq__(self, __value: object) -> bool:
        assert isinstance(__value, Rectangle)
        return self.a == __value.a and self.b == __value.b

    def __hash__(self) -> int:
        return 5


def test_operation_in(collection: list | set):
    rand = random.randint(0, len(collection))
    # // TODO doplňte testování, zda je náhodně vybraný prvek v kolekci

    if rand in collection:
        pass


def test_collection(our_collection: list | set, test_function: Callable[[list | set], None]):
    elapsed_in = 0.0
    # // TODO doplňte měření času pro testovací funkci pomocí timeit

    elapsed_in = timeit.timeit(
        lambda: test_function(our_collection), number=N_TESTS)

    return elapsed_in


def experiment_eq_and_hash():
    rectangles = list([Rectangle(1, 1), Rectangle(1, 2)])
    # TODO naplňte list několika obdélníky. Následně vytvořte nový obdélník, který má stejné parametry jako některý z obdélníků v listu a zjistěte, zda je v listu pomocí operátoru in

    assert Rectangle(1, 1) in rectangles
    assert Rectangle(1, 2) in rectangles


def experiment_with_operations():
    # pro vizualizaci výsledků
    structure_sizes = list()
    times = list()
    structure_types = list()

    # // TODO doplňte měření času pro list a set pro různé velikosti kolekcí (krok po 10 % velikosti COLLECTION_SIZE), uložte si výsledky a poté je vizualizujte

    sizes = range(COLLECTION_SIZE // 10,
                  COLLECTION_SIZE, COLLECTION_SIZE // 10)
    for collection_size in sizes:

        tested_list = list(range(collection_size))
        list_time = test_collection(tested_list, test_operation_in)

        structure_sizes.append(collection_size)
        times.append(list_time)
        structure_types.append("List")

        tested_set = set(tested_list)
        set_time = test_collection(tested_set, test_operation_in)

        structure_sizes.append(collection_size)
        times.append(set_time)
        structure_types.append("Set")

    # vizualizace výsledků
    plot_data = {
        'Structure size': structure_sizes,  # osa x - velikost kolekce
        'Time': times,                   # osa y - časy
        # typ kolekce (list/set) pro barevné rozlišení
        'Data Structure':  structure_types
    }

    fig = px.line(plot_data, x='Structure size', y='Time', color='Data Structure',
                  title='Time Comparison of List vs Set Operations')
    fig.show()


if __name__ == "__main__":
    experiment_with_operations()
    experiment_eq_and_hash()
