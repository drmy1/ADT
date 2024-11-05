# pipem nainstalovat
# https://github.com/JakubSido/adthelpers
# pip install git+https://github.com/JakubSido/adthelpers


"""
Zadání:
   Dodaná data obsahují informace o geologické oblasti na území Česka. Jedná se o data z místa rekultivovaného
   po důlní činnosti. Uzly představují nově vytvořené stavební parcely určené pro rekreační objekty na břehu
   nově plánovaného jezera. Vzhledem k předchozí důlní činnosti jsou kladené přísné podmínky na možnost dalších
   výkopových prací a tato činnost je významně omezena a kontrolována z důvodu potenciálně nestabilního podloží.
   Vaším úkolem je navrhnout nejlevnější řešení pro zajištění připojení k elektrické síti pro každou parcelu.
   V souboru je pro každou parcelu a jí přilehlé parcely uvedena odhadovaná cena zřízení rozvodů s přihlédnutím
   k aktuální geologické situaci při dodržení přísných požadavků na bezpečnost prací.

   Cílem vaší práce je dostat program do stavu, kdy bude hledat nejlevnější realizaci elektrické rozvodné sítě.
   Doplňte případné chybějící importy
   Implementujte chybějící části kódu a opravte případné chyby
   Dodržte signaturu funkcí (argumenty funkcí, návratové typy). Neměňte typy, počet argumentů ani návratové typy funkcí.
   Neměňte jména funkcí ani tříd. Pro implementaci veškeré funkcionality využijte připravené funkce, třídy a jejich metody.

Formát Dat:
  - soubor edges.csv obsahuje informaci o odhadovaných cenách elektrické sítě mezi sousedními parcelami.
      - source a target jsou označení parcel,
      - weight je cena zřízení rozvodu mezi dvěma parcelami
  - soubor nodes.csv obsahuje výčet všech parcel (Neobsahuje žádnou informaci navíc oproti edges.csv. K vyřešení úlohy není potřebný).


Hodnocení:
    Pozn.: Třída reprezentující Graf a Vrcholy je elementární funkcionalita. Bez jejich správného fungování
    není možné váš program dále hodnotit.Věnujte proto zvýšenou pozornost této části.

    Správně načtené parametry z cmd [+1/1]  passed
    Funkční main - vrací správný výsledek [+1/1]    passed
    Funkční graf se správným rozhraním [+3/3]    passed
        Graph  create_edge  - node count (add_duplicity=False) [+1/1]   passed
        Graph  create_edge  - node count (add_duplicity=True) [+1/1]    passed
        Graph - undirected?  [+1/1]     passed
    Správné načtení grafu [+5]    passed
        Load graph - nodes and edges count [+4/4]       passed
        Load graph - weights on edges [+1/1]    passed
    Správně nalezené řešení [+6]   passed
        Find optimal solution own_load=False [+3/3]     passed
        Find optimal solution own_load=True [+3/3]      passed
    Správně spočtená cena řešení [+4]     passed
        Evaluate solution own_load=True own_find_solution=True [+2/2]   passed
        Evaluate solution own_load=False own_find_solution=False [+2/2] passed
"""

from queue import PriorityQueue
import sys
import os


class Vertex:
    """Třída reprezentující vrchol grafu.
    self.id je identifikátor vrcholu.
    self.edges je seznam hran, které vedou z tohoto vrcholu."""

    def __init__(self, id) -> None:
        self.id: int = id  # identifikátor uzlu
        self.edges: list[tuple[float, Vertex]] = (
            list()
        )  # (váha hrany, (kam_se_dostanu))


class UndirectedGraph:
    """
    Třída reprezentující neorientovaný graf.
    self.vertices a self.edges použijte pro uložení grafu: Neměňte jméno ani typ proměnných!!!
    Správně je inicializujte v konstruktoru a použijte v metodách __add_node a __add_edge.
    """

    def __init__(self) -> None:
        self.vertices: dict[int, Vertex] = dict()
        self.edges: dict[tuple[int, int], float] = dict()

    def __add_node(self, vertex: Vertex):
        """Metoda přidá node do grafu.
        Args:
            node (Vertex): uzel, který se má přidat do grafu
        """
        # // TODO Implementujte metodu dle specifikace
        self.vertices[vertex.id] = vertex

    def __add_edge(self, src: Vertex, dst: Vertex, weight: float = 0):
        """Metoda přidá hranu mezi dva uzly v grafu. Hrana je neorientovaná.
        Args:
            src (Vertex): Uzel, ze kterého hrana vede
            dst (Vertex): Uzel, do kterého hrana vede
            weight (float, optional): Ohodnocení hrany. Defaults to 0.
        """
        # // TODO Implementujte metodu dle specifikace
        src.edges.append((weight, dst))
        dst.edges.append((weight, src))
        self.edges[(src.id, dst.id)] = weight

    def create_edge(self, src_id: int, dst_id: int, weight: float = 0):
        """Metoda přidá hranu do grafu. Vstupují identifikátory uzlů. Pokud uzly neexistují, vytvoří je.
        Interně volá metody __add_node a __add_edge.

        Args:
            src_id (int): Identifikátor uzlu, ze kterého hrana vede.
            dst_id (int): Identifikátor uzlu, do kterého hrana vede.
            weight (float, optional): Ohodnocení hrany. Defaults to 0.
        """
        # // TODO Implementujte metodu dle specifikace
        if src_id not in self.vertices:
            src_node = Vertex(src_id)
            self.__add_node(src_node)
        if dst_id not in self.vertices:
            dst_node = Vertex(dst_id)
            self.__add_node(dst_node)

        self.__add_edge(self.vertices[src_id], self.vertices[dst_id], weight)


def load_graph(edge_filepath: str) -> tuple[UndirectedGraph, dict]:
    """Načte graf a metadata ze souboru.
    Protože datový typ identifikátoru parcely není celé číslo, kromě grafu se vrací také slovník, který uchovává původní identifikátory.
    Pro formát souboru viz hlavičku souboru. Případné vadné záznamy přeskočte (špatný počet záznamů na řádku, špatný datový typ).

    Returns:
        tuple[UndirectedGraph, dict] :
            graph : UndirectedGraph : instance třídy UndirectedGraph obsahující načtená data
            mapping : dict : slovník obsahující mapování identifikátorů parcel na uzly v grafu. Klíčem je původní identifikátor (např. 1051c), hodnotou je id uzlu.
    """
    # source weight target
    # 1000c?97?1020c
    # {"1000c": 1000}

    graph = UndirectedGraph()
    mapping: dict[str, int] = dict()
    dup: list[tuple] = list()
    with open(edge_filepath) as file_desc:
        file_desc.readline()
        lines = file_desc.read()
        for line in lines.split("\n"):
            if line == "":
                continue
            splittedline = line.split("?")
            source = splittedline[0]
            weight = int(splittedline[1])
            target = splittedline[2]
            source_int = source.strip("abcdefghijklmnopqrstuvwxyz")
            target_int = target.strip("abcdefghijklmnopqrstuvwxyz")
            if (source_int, target_int, weight) not in dup:
                dup.append((source_int, target_int, weight))
                mapping[source] = int(source_int)
                graph.create_edge(
                    int(source_int),
                    int(target_int),
                    weight,
                )
    return graph, mapping


def evaluate_solution(graph: UndirectedGraph, solution: set[tuple[int, int]]) -> float:
    """Funkce vypočítá reálnou cenu nalezeného řešení. Vstupem je graf a množina hran, které tvoří řešení.

    Args:
        graph (UndirectedGraph): Instance třídy UndirectedGraph obsahující načtená data (výstup funkce load_graph)
        solution (set[tuple[int, int]]): Množina dvojic sousedních pozemků, které budou propojeny v nejlevnějším řešení.

    Returns:
        float: Celková cena řešení vyčíslená jako součet cen jednotlivých hran.
    """
    price = 0.0
    for edge in solution:
        edge = (min(edge), max(edge))
        price += graph.edges[edge]

    return price


def find_solution(graph: UndirectedGraph) -> set[tuple[int, int]]:
    """Funkce nalezne nejlevnější řešení pro propojení všech pozemků pro vybudování sítě.

    Args:
        graph (UndirectedGraph): Instance třídy UndirectedGraph obsahující načtená data

    Returns:
        set[tuple[int, int]]: Množina dvojic sousedních pozemků, které budou propojeny
        v nejlevnějším řešení.
    """

    # // TODO nezapomente, ze pokud pouzivate pro inicializaci fronty nějakou "virtuální hranu", není součástí řešení

    electrical_wiring: set[tuple[int, int]] = set()
    closed = set()

    queue: PriorityQueue = PriorityQueue()

    next_item = (0, (1000, 1020))  # (váha hrany, (odkud_id, kam_id))

    queue.put(next_item)

    actual_node = None
    while (
        queue.qsize() > 0
    ):  ## pokud sem umístíme breakpoint, můžeme sledovat jak se algoritmus vyvíjí
        # vyberu hranu s nejmenším ohodnocením, o to se stará prioritní fronta. Ohodnocení samotné (první část)
        # už nepotřebujeme používá se pro účely prioritní fronty (řazení). Dále pracujeme jen s hranou (druhá část)
        # Tato hrana je dobrý kandidát na přidání do kostry.
        _, edge = queue.get()
        _, actual_id = edge

        # Check if the actual_id is a valid vertex in the graph
        if actual_id not in graph.vertices:
            continue

        actual_node = graph.vertices[actual_id]

        # Pokud je uzel na konci uvažované hrany už zpracovaný - objevený odjinud dříve (přístupný z kostry),
        # zahazuji ji a beru si další. V opačném případě bych vytvořil cyklus v grafu a kostru si poničil.
        if actual_id in closed:
            continue

        # Hranu přidám do kostry
        electrical_wiring.add(edge)

        # přidám všechny nově objevené hrany do fronty
        for weight, to_id in actual_node.edges:
            next_item = (int(weight), (actual_node.id, to_id.id))
            queue.put(next_item)

        closed.add(actual_id)  # uzel je zpracovaný

    return electrical_wiring


def find_key(node, mapping: dict[str, int]):
    for key in mapping.keys():
        if node == mapping[key]:
            return key


def generate_plan(
    solution: set[tuple[int, int]], mapping: dict[str, int]
) -> set[tuple[str, str]]:
    """Z nalezeného řešení (interní reprezentace uzlů jako int) vygeneruje plán pro vedení stavby ve
    formátu původních identifikátorů uvedených v souboru.
    Args:
        solution (set[tuple[int, int]]): nalezený výsledek (výstup funkce find_solution)
        mapping (dict[str, int]): mapování původních identifikátorů na interní reprezentaci (výstup funkce load_graph)

    Returns:
        set[tuple[str, str]]: Seznam dvojic vedlejších parcel, které je se mají propojit elektrickým vedením.


    """
    new_solution = set()
    for edge in solution:
        from_node, to_node = edge

        new_from_node = find_key(from_node, mapping)
        new_to_node = find_key(to_node, mapping)

        new_edge = (new_to_node, new_from_node)
        new_solution.add(new_edge)

    return set(new_solution)


def main(datapath):
    edge_path = os.path.join(datapath)

    graph, mapping = load_graph(edge_path)
    best_solution = find_solution(graph)

    print(best_solution)
    price = evaluate_solution(graph, best_solution)
    print(price)

    plan = generate_plan(best_solution, mapping)
    print(plan)


if __name__ == "__main__":
    # Program přijímá cestu ke složce s daty. Bude spouštěn následujícím příkazem "python main.py some/path_to/data/folder"
    # // TODO implementujte zpracování argumentu z příkazové řádky.
    if (len(sys.argv) - 1) == 1:
        datapath = sys.argv[1]
    else:
        raise ValueError("wrong number of arguments")
    main(datapath)
