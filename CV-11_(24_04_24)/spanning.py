# pipem nainstalovat
# https://github.com/JakubSido/adthelpers
# pip install git+https://github.com/JakubSido/adthelpers
import json
import adthelpers

from queue import PriorityQueue


class Node:
    def __init__(self, id) -> None:
        self.id: int = id  # identifikátor uzlu
        self.neighbors: list[tuple[float, Node]] = list()  # (váha hrany, (kam_se_dostanu))


class Graph:
    def __init__(self) -> None:
        self.nodes: dict[int, Node] = dict()
        self.edges: set = set()

    ##MSBE##

    def add_node(self, node: Node):
        self.nodes[node.id] = node  ##MASK_RM##

    def add_edge(self, src: Node, dst: Node, weight=0):
        src.neighbors.append((weight, dst))
        dst.neighbors.append((weight, src))
        self.edges.add((weight, src, dst))

    def add_edge_id(self, src_id: int, dst_id: int, weight: float = 0):
        if src_id not in self.nodes:
            src_node = Node(src_id)
            self.add_node(src_node)
        if dst_id not in self.nodes:
            dst_node = Node(dst_id)
            self.add_node(dst_node)

        self.add_edge(self.nodes[src_id], self.nodes[dst_id], weight)


def load_graph(filepath: str) -> Graph:
    graph = Graph()
    with open(filepath, "r", encoding="utf8") as fd:
        file_string = fd.read()
        js = json.loads(file_string)

        for n in js["nodes"]:
            node_id = Node(n["id"])
            graph.add_node(node_id)

        for e in js["links"]:
            graph.add_edge(graph.nodes[e["source"]], graph.nodes[e["target"]], e["weight"])
    return graph
    ##MSBE##
    return None


def main():

    graph = load_graph("data/graph_grid_s3_3.json")
    painter = adthelpers.painter.Painter(graph)
    painter.draw_graph()
    input("Press Enter to continue...")

    spanning_tree = set()
    closed = set()
    q = PriorityQueue()

    # pro ucely vizualizace
    painter = adthelpers.painter.Painter(
        graph,
        visible=q,
        closed=closed,
        color_edges=spanning_tree,
    )
    painter.draw_graph()  # pokaždé když zavolame draw_graph() vynutíme překreslení

    next_item = (0, (None, 0))  # (váha hrany, (odkud_id, kam_id))
    q.put(next_item)

    actual_node = None
    while q.qsize() > 0:  ## pokud sem umístíme breakpoint, můžeme sledovat jak se algoritmus vyvíjí

        _, e = q.get()
        from_id, to_id = e
        to_node = graph.nodes[to_id]
        if to_node in closed:
            continue
        actual_node = graph.nodes[to_id]

        spanning_tree.add(e)

        if actual_node in closed:
            continue

        painter.draw_graph(actual_node)

        for weight, to_id in actual_node.neighbors:  # přidám všechny nově objevené hrany do fronty
            next_item = (weight, (actual_node.id, to_id.id))
            q.put(next_item)
            painter.draw_graph()

        closed.add(actual_node)

    ##MSBE##


if __name__ == "__main__":
    main()
    input("Press Enter to continue...") 

