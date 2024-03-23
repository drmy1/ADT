from collections import defaultdict
import os
import sys
from typing import Optional


class Record():
    def __init__(self, time: int, id_cost: int, ckpt: str) -> None:
        self.time = time
        self.id_cost = id_cost
        self.ckpt = ckpt


def load_data(datapath: str, city: str, shop: str, day: Optional[str] = "1-Mon") -> dict[str, list[Record]] | None:
    # doporučujeme jako klíč použít název checkpointu

    city_data = defaultdict(lambda: list())

    datapath = os.path.join(datapath, city, str(day), f"{shop}.txt")
    if not os.path.exists(datapath):
        print("soubor neexistuje", datapath)
        return None

    with open(datapath, 'r', encoding="utf8") as f:
        f.readline()
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            field = line.split(";")
            try:
                r = Record(int(field[0]), int(field[2]), field[1])
                key = f"{r.ckpt}"
                city_data[key].append(r)
            except ValueError as e:
                print("chyba v souboru ValueError neocekavana hodnota",
                      datapath, "\n", line)
                continue

    print("loading", city)

    return city_data


def get_passed_set(data: dict[str, list[Record]], key_words: list[str]) -> set[int]:
    costumers = set()
    return costumers


def filter_data_time(data: dict[str, list[Record]], cond_time: int) -> dict[str, list[Record]]:
    ret = defaultdict(lambda: list())
    return ret


def get_q_size(data: dict[str, list[Record]], seconds: int) -> int:
    queue = set()
    return len(queue)


def histogram(data: dict[str, list[Record]]):
    pass


def main(datadir):

    data = None

    while True:
        city = str(input("Zadej město: "))
        shop = str(input("Zadej obchod: "))
        data = load_data(datadir, city, shop)
        if data is None:
            print("Nesprávný vstup")
            pass


if __name__ == "__main__":
    datadir = ""

    if len(sys.argv) != 2:
        print("invalid data path")
        exit(1)

    datadir = sys.argv[1]

    if not os.path.exists(datadir):
        print("invalid data path")
        exit(2)

    main(datadir)
