from utils import measure_time


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def fib_mem(n: int, lookup: dict[int, int]) -> int:
    if n <= 1:
        return n
    if n in lookup:
        return lookup[n]
    lookup[n] = fib_mem(n-1, lookup) + fib_mem(n-2, lookup)
    return lookup[n]


def main():
    n = 30

    print(measure_time(lambda: fib(n)))
    lookup = dict()
    print(measure_time(lambda: fib_mem(n, lookup)))


if __name__ == "__main__":
    main()
