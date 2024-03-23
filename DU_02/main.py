
import seaborn as sns
from typing import List, Tuple


# vstupem budou úseky ze zadání [(20,.5),(1,-5),(10,2)]
def simulate(accelerations: List[Tuple[int, int]]):
    distance = 0  # počáteční vzdálenost
    speed = 0  # počáteční rychlost

    speeds = list()
    distances = list()
    for duration, accelerate in accelerations:  # pro jednotlivé úseky zrychlení ze zadání
        for second in range(duration):  # pro každou sekundu v daném úseku
            # uložíme si aktuální hodnoty pro vizualizaci (okamžitá rychlost (speeds) a vzdálenost od počátku (distances))

            # TODO vypočítejte aktuální rychlost, tak, že na aktuální hodnotu rychlosti aplikujete zrychlení
            speeds = speed + (accelerate * second) / abs(accelerate)

            # TODO vypočítejte přírůstek vzdálenosti za jednotku času a přidejte jej do již uražené vzdálenosti
            distances = speed * duration

            # TODO uložíme si aktuální hodnoty pro vizualizaci (okamžitá rychlost a vzdálenost od počátku)

            # vypíšeme si aktuální hodnoty
            print(f"{second=} {speed=} {distance=}")

    return speeds, distances


accelerations = [(20, .5), (1, -5), (10, 2)]
speeds, distances = simulate(accelerations)


# x roste od 0 do počtu prvků v seznamu, y je seznam rychlostí
sns.lineplot(x=range(len(speeds)), y=(speeds))

# x roste od 0 do počtu prvků v seznamu, y je seznam vzdáleností
sns.lineplot(x=range(len(speeds)), y=(distances))