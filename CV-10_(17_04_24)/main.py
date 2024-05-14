# pipem nainstalovat
# https://github.com/JakubSido/adthelpers
# pip install git+https://github.com/JakubSido/adthelpers
import json  # noqa Flake8 (ignore unused inport)
import adthelpers  # type: ignore

from queue import PriorityQueue


class Node:
    def __init__(self, id) -> None:
        # // TODO 1
        self.id: int = id  # identifikátor uzlu
        # (váha hrany, (kam_se_dostanu))
        self.neighbors: list[tuple[float, Node]] = list()


class Graph:
    def __init__(self) -> None:
        # // TODO 2
        self.nodes: dict[int, Node] = dict()
        self.edges: list[tuple[float, Node, Node]] = list()

    def add_node(self, node: Node):
        # // TODO 3
        self.nodes[node.id] = node

    def add_edge(self, src: Node, dst: Node, weight=0):
        # // TODO 4
        src.neighbors.append((weight, dst))
        dst.neighbors.append((weight, src))
        self.edges.append((weight, src, dst))


def load_graph(filepath: str) -> Graph:
    # // TODO 5
    graph = Graph()

    with open(filepath, "r") as f:
        json_data = json.load(f)
        for node_id in json_data["nodes"]:
            node = Node(node_id["id"])
            graph.add_node(node)

        for link in json_data["links"]:
            src = graph.nodes[link["source"]]
            dst = graph.nodes[link["target"]]
            weight = link["weight"]
            graph.add_edge(src, dst, weight)

    return graph


def main():

    graph = load_graph("data/graph_grid_s3_3.json")
    painter = adthelpers.painter.Painter(graph)
    painter.draw_graph()

    input("Press Enter to continue...")


if __name__ == "__main__":

    main()
    input("Press Enter to continue...")
