import os


def load_data(filename: str) -> list:
    if not os.path.exists(filename):
        return list()

    people = list()
    with open(filename, encoding="utf8") as f:
        for line_number, line in enumerate(f):

            # ! TODO pridejme podmínku, která přeskočí první řádek v souboru
            if line_number == 0:
                continue

            line = line.strip()
            data = line.split(",")

            # v předchozím cvičení jsme si všechny hodnoty uložili do proměnných,
            # nyní uložíme celý rozdělený do seznamu lidí
            # jmeno, prijmenni, vek, vaha = data
            people.append(data)
    return people


def count_avg_weight(people: list) -> float:
    weight_sum = 0.0
    weight_count = 0
    for person in people:
        firstname, lastname, weight, height, age = person
        # ! TODO na dvou následujících řádcích přičtěme váhu a zvýšeme počet osob
        weight_sum += float(weight)
        weight_count += 1
    return weight_sum/weight_count


# Nejlepší na tom je to, že pro spočtení osob, které mají podprůměrnou váhu, už máme polovinu práce hotovou (načtení dat).
# Vhodnou dekompozicí si tedy můžeme velice usnadnit práci.
# Nyní stačí jenom projít všechny osoby a spočítat ty, které mají váhu menší než je průměrná.
# Vytvoříme tedy novou funkci filter_people_by_weight
# Vstup seznam osob, limitní váha
# Výstup: seznam osob, které mají váhu menší než je limitní váha
def filter_people_by_weight(people: list, limit: float) -> list:
    filtered_people: list = list()
    for person in people:

        # všimněme si, že funkce počítá, že data přichází v konkrétním pořadí.
        # pokud bychom dostali soubor v jiném formátu, mohli bychom narazit na problém.
        firstname, lastname, weight, height, age = person
        weight = float(weight)
        if float(weight) < limit:
            filtered_people.append(person)
            pass
    return filtered_people


def max_age_person(people: list) -> tuple:
    top_age = 0
    grandpa = None
    for person in people:
        firstname, lastname, weight, height, age = person
        age = int(age)
        weight = float(weight)
        if int(age) > top_age:
            top_age = age
            grandpa = person
    return grandpa


if __name__ == "__main__":
    # vstupní soubor
    DATA_FILE = "data.csv"

    # Následující 2 řádky jsou tu pouze pro testovací účely naším validátorem. Pouze říkají, že
    # pokud existuje systémová proměnná DATA_FILE, pak se cesta k souboru přepíše její hodnotou.
    if "DATA_FILE" in os.environ:
        DATA_FILE = os.environ["DATA_FILE"]

    people = load_data(DATA_FILE)
    avg_weight = count_avg_weight(people)
    light_people = filter_people_by_weight(people, avg_weight)

    # ! TODO na následujícím řádku vyplňme počet prvků v seznamu
    n_of_light_people = len(light_people)
    print(f"Počet osob s podprůměrnou váhou je: {n_of_light_people}")
    print(f"Průměrná váha osob v souboru je :{avg_weight}")

    light_weighted_grandpa = max_age_person(light_people)
    print(f"Nejstarší osoba s podprůměrnou váhou je: {light_weighted_grandpa}")
