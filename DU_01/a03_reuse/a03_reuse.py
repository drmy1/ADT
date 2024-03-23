import os
from a02_load_filter_in_memory import load_data
from typing import Callable


def is_obese(person: list) -> bool:
    firstname, lastname, weight, height, age = person
    bmi = 0.0
    bmi = float(weight) / ((int(height)/100)**2)  # <--- tato řádka nám způsobí problémy
    print(f"bmi: {bmi}")
    if bmi < 30:
        return False
    else:
        return True


def filter(people: list, filter_function: Callable[[list[str]], bool]) -> list:
    filtered_people = list()
    for person in people:
        if filter_function(person):
            filtered_people.append(person)

    return filtered_people


if __name__ == "__main__":
    DATA_FILE = "data.csv"

    # Následující 3 řádky jsou tu pouze pro testovací účely naším validátorem. Pouze říkají, že
    # pokud existuje systémová proměnná DATA_FILE, pak se cesta k souboru přepíše její hodnotou.
    if "DATA_FILE" in os.environ:
        DATA_FILE = os.environ["DATA_FILE"]

    people = load_data(DATA_FILE)
    print(people[:4])
    print(f"je 1. obezni? {is_obese(people[1])}")
    print(f"je 2. obezni? {is_obese(people[2])}")

    filtered_people = filter(people, is_obese)
    print(filtered_people[:4])
