import collections
import random


class NamedQueue():
    name: str
    queue: collections.deque

    def __init__(self, name: str) -> None:
        self.name = name
        self.queue = collections.deque()


class ProcessingNode:
    name: str
    source: NamedQueue
    destination: NamedQueue
    amount: int
    period_mean: int
    period_sigma: float
    __remaining_time: int

    def __init__(self, name: str, period: int, source: NamedQueue, destination: NamedQueue, amount=1, sigma=0.1) -> None:
        self.name = name
        self.source = source
        self.destination = destination
        self.amount = amount
        self.period_mean = period
        self.period_sigma = sigma * period
        self.__remaining_time = 0

    def step(self):
        self.__remaining_time -= 1

    def reset_node(self):
        self.__remaining_time = int(random.gauss(
            self.period_mean, self.period_sigma))

    def update(self):
        self.step()

        if self.__remaining_time <= 0:
            self.perform()
            self.reset_node()

    def perform(self):
        to_pop = min(self.amount, len(self.source.queue))
        for _ in range(to_pop):
            processed_item = self.source.queue.popleft()
            self.destination.queue.append(processed_item)


class Observer:
    __queues_to_observe: list[NamedQueue]

    def __init__(self, list_to_observe):
        self.__queues_to_observe = list_to_observe

    def take_snapshot(self):
        state_strings = []

        for q in self.__queues_to_observe:
            state_strings.append(f"{na}: {q.queue}")


def main():
    NUMBER_OF_PEOPLE = 10000

    street_queue = NamedQueue("street")
    street_queue.queue = collections.deque(
        [i for i in range(NUMBER_OF_PEOPLE)])

    gate_q = NamedQueue("gate")
    vege_q = NamedQueue("meat")
    final_q = NamedQueue("final")

    done_queue = NamedQueue("done")

    simulation_nodes = [
        ProcessingNode("usual_day", 60, street_queue, gate_q, 1),
        ProcessingNode("gate_keeper", 0, gate_q, vege_q, 1),
        ProcessingNode("vege_X", 10, vege_q, final_q, 1),
        ProcessingNode("final", 10, final_q, done_queue, 1),
    ]

    for time in range(60 * 60):
        for node in simulation_nodes:
            node.update()

        # // TODO: podívejme se na stav obchodu v nějakých časových intervalech
        if time % 60 == 0:
            hours = time * 60 * 60
            minutes = time * 60
            snapshot = Observer(simulation_nodes)
            print(f"{hours:02d}:{minutes:02d}:{snapshot}")


if __name__ == "__main__":
    main()
