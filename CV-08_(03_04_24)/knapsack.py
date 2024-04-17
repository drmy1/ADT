

def load_data(path) -> tuple[list[float], list[float]]:
    values: list[float] = []  # rating
    weights: list[float] = []  # délky v sekundách

    with open(path, "r") as file:
        for line in file:
            line = line.strip("\n")
            splittedline = line.split(" ")
            values.append(float(splittedline[0]))
            weight = splittedline[1].split(":")
            weights.append(float(weight[0]) * 60 + float(weight[1]))

        return values, weights


def knapsack_backtrack(n: int, weight_res: float, weights: list[float], values: list[float]):
    n = 0
    sum_weight = 0.0
    if sum_weight >= weight_res:
        return n
    else:
        n += 1
        
        sum_weight += weights[n]


def main():
    values, weights = load_data("data/songs copy.txt")
    raiting = knapsack_backtrack(0, 4*60, weights, values)
    print(raiting)


if __name__ == "__main__":
    main()
