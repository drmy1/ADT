import argparse
from collections import defaultdict
from pathlib import Path
from typing import Final, Optional
from dataclasses import dataclass


import plotly.express as px  # type: ignore


# // TODO: Vytvořte třídu `Record` s atributy vyjmenovanými v sekci 1 v souboru `README.md`

@dataclass
class Record:
    time: int
    checkpoint_id: str
    customer_id: int
    money: Optional[int] = None


# Hint: alias typu pro lepší čitelnost a udržitelnost kódu
CheckpointDict = dict[str, list[Record]]


CITY: Final[str] = "Plzeň"


def load_records(data_path: Path, day: str, shop: str) -> CheckpointDict:
    data: CheckpointDict = defaultdict(list)

    shop_data_path = data_path / CITY / day / f"{shop}.txt"
    with open(shop_data_path, "r", encoding="utf8") as file_desc:
        # přeskočení hlavičky
        file_desc.readline()

        for line in file_desc:
            # odstranění bílých znaků na začátku a konci řádku
            line = line.strip()

            splitted_line = line.split(";")
            try:
                r = Record(
                    time=int(splitted_line[0]),
                    checkpoint_id=splitted_line[1],
                    customer_id=int(splitted_line[2]),
                    money=(
                        int(splitted_line[3])
                        if len(splitted_line) > 3 and splitted_line[3].isnumeric()
                        else None
                    )
                )
            except ValueError:
                print(f"Invalid record in file: `{shop_data_path}`")
                continue

            # přidáme záznam do slovníku
            data[r.checkpoint_id].append(r)

    return data


def get_passed_customers(data: CheckpointDict, checkpoint_names: list[str]) -> set[int]:
    # Hint: ve slovníku `data` máme pro každý checkpoint seznam záznamů (zákazníků), které jím prošly
    # Hint: jméno checkpointu `checkpoint_name` můžete získat z `checkpoint_id` pomocí `split("_")[0]`

    customers = set()

    # // TODO: zajistěte, aby funkce vrátila množinu identifikátorů zákazníků, kteří prošli všemi checkpointy v `checkpoint_ids`

    for checkpoint_id, records in data.items():
        checkpoint_name = checkpoint_id.split("_")[0]

        if checkpoint_name not in checkpoint_names:
            continue

        for record in records:
            customers.add(record.customer_id)

    return customers


def filter_data_by_time(data: CheckpointDict, until_time: int) -> CheckpointDict:
    filtered_data: CheckpointDict = defaultdict(list)

    # // TODO: získejte záznamy jejichž atribut `time` je ostře větší než `until_time`
    for checkpoint_id, records in data.items():
        for record in records:
            if record.time > until_time:
                break

            filtered_data[checkpoint_id].append(record)

    return filtered_data


def get_queue_size(records: CheckpointDict, time: int) -> int:
    # získáme data do času `time`
    filtered_data = filter_data_by_time(records, time)

    # získáme zákazníky, kteří prošli checkpointy `vege`, `frui` a `meat`
    checkpoint_names = ["vege", "frui", "meat"]
    first = get_passed_customers(filtered_data, checkpoint_names)

    # získáme zákazníky, kteří prošli checkpointem `final-crs`
    checkpoint_names = ["final-crs"]
    second = get_passed_customers(filtered_data, checkpoint_names)

    # Jak získáme množinu zákazníků ve frontě `first`?
    queue = first.difference(second)
    return len(queue)


def histogram(records: CheckpointDict) -> list[int]:
    # // TODO: získejte histogram fronty zákazníků pro každou hodinu v den

    histogram = []
    for hour in range(0, 24):
        queue_size = get_queue_size(records, hour * 60 * 60)
        histogram.append(queue_size)

    # return [get_queue_size(records, hour * 60 * 60) for hour in range(0, 24)]
    return histogram


def plot_histograms(histograms: dict[str, list[int]]) -> None:
    fig = px.line(
        histograms,
        labels={"variable": "Město", "index": "Čas", "value": "Zákazníků ve frontě"},
        title="Porovnání front zákazníků v různých městech",
    )
    fig.show()


def main(data_path: Path, day: str, shop: str) -> int:
    if not data_path.exists() or not data_path.is_dir():
        print(f"Path `{data_path}` does not exist or is not a directory")
        return 1

    # načtení záznamů z daného adresáře
    records = load_records(data_path, day, shop)

    histograms = {
        CITY: histogram(records)
    }
    plot_histograms(histograms)

    return 0


if __name__ == "__main__":
    # použití standardního modulu `argparse` pro zpracování argumentů
    arg_parser = argparse.ArgumentParser(description="")
    arg_parser.add_argument("--data_path", type=Path, help="Cesta k adresáři s daty.")
    arg_parser.add_argument("--day", type=str, help="Den, ze kterého se mají zpracovat data.")
    arg_parser.add_argument("--shop", type=str, help="Obchod, ze kterého se mají zpracovat data.")

    # zpracování argumentů
    args = arg_parser.parse_args()

    # spuštění funkce `main` s argumenty
    # všimněte si použití operátoru rozbalení pojmenovaných argumentů
    exit_code = main(**vars(args))

    # skript ukončíme s návratovým kódem
    exit(exit_code)
