import os


def load_data_and_count_mean(filename: str) -> float:

    # otevřeme soubor (mohli bychom ověřovat, že soubor existuje, ale pro jednoduchost to nebudeme dělat)
    with open(filename, encoding='utf-8') as f:

        # inicializujeme proměnné, do kterých budeme ukládat mezivýsledek
        weight_sum = 0.0   # čitatel
        weight_count = 0  # jmenovatel

        # projdeme všechny řádky souboru, které představují jednotlivé osoby
        for line_number, line in enumerate(f):
            # první řádek (počítáno od nuly) neobsahuje osobu, ale hlavičku,
            if line_number == 0:
                continue        # proto ho přeskočíme

            # každý řádek má na konci speciální znak \n (konec řádku), toho se zbavíme pomocí funkce strip
            # funkce vrací nový řetězec, který je bez znaku \n
            line = line.strip()

            # vyčištěný řádek rozdělíme pomocí čárky, funkce nám vrátí seznam hodnot (jméno, prijmenni, vek, vaha)
            data = line.split(",")

            # všechny hodnoty si uložíme do proměnných, všechno jsou to řetězce (string)
            firstname, lastname, weight, height, age = data

            # ! TODO následující řádku upravte tak, aby se do proměnné weight_sum přičetla váha osoby
            # pozn. protože chceme spočítat průměr, musíme řetězec převést na desetinné číslo abychom byli schopni numericky sčítat
            weight_sum += float(weight)
            weight_count += 1

    # ! TODO následující řádky upravte tak, aby funkce vracela průměr
    average = weight_sum / weight_count
    return average


if __name__ == "__main__":

    # vstupní soubor
    DATA_FILE = "data.csv"

    # Následující 2 řádky jsou tu pouze pro testovací účely naším validátorem. Pouze říkají, že
    # pokud existuje systémová proměnná DATA_FILE, pak se cesta k souboru přepíše její hodnotou.
#    if "DATA_FILE" in os.environ:
#        DATA_FILE = os.environ["DATA_FILE"]

    avg_weight = load_data_and_count_mean(DATA_FILE)
    print(f"Průměrná váha osob v souboru je :{avg_weight}")
