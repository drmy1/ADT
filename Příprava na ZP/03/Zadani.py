"""
Zadání:
    - Zastupitelstvo města České Budějovice získalo dotaci na podporu turistiky a rádo by zřídilo speciální
    - vlakovou linku pro podporu cyklistů cestující do Národního parku Šumava. Pro splnění dotačního programu
    - musí přesně vyčíslit vzdálenost, kterou by linka <České Budějovice-Vimperk> měla jezdit. Kudy by linka
    - musela jezdit, aby byla co nejkratší. Jak dlouhá by taková cesta byla?
    - Cílem vaší práce je dostat program do stavu, kdy bude hledat nejkratší cestu obecně mezi zastávkami v české železniční síti.
    - Doplňte případné chybějící importy
    - Implementujte chybějící části kódu a opravte případné chyby
    - Dodržte signaturu funkcí (argumenty funkcí, návratové typy). Neměňte typy, počet argumentů ani návratové typy funkcí.
    - Neměňte jména funkcí ani tříd. Pro implementaci veškeré funkcionality využijte připravené funkce třídy a jejich metody.

DATA:
Dodaná data obsahují neorientovaný graf českých železničních koridorů. Data jsou uložena ve dvou souborech.
  - soubor edges.csv obsahuje informaci o železničních trasách. Každý řádek souboru obsahuje informaci o jedné trase z bodu A do bodu B.
      - source a target jsou identifikátory železničních uzlů, které spojuje,
      - clength je ohodnocení (délka) hrany v metrech,
      - ostatní pole pro tento úkol nejsou důležitá.
  - soubor nodes.csv obsahuje informaci o vlakových zastávkách. Každý řádek souboru obsahuje informaci o jedné zastávce. Pokud neexistuje pro některý z bodů
  ze souboru edges záznam v nodes, jedná se o průjezdní bod. Vlak zde nezastavuje.
      - id je identifikátor vrcholu,
      - sname je název stanice.
      - ostatní pole pro tento úkol nejsou důležité

Hodnocení:
    - Pozn. Třída reprezentující Graf a Vrcholy je elementární funkcionalita. Bez jejich správného fungování
    není možné váš program dále hodnotit. Věnujte proto zvýšenou pozornost této části.

    - Funkční graf se správným rozhraním - 3 body
    - Správné načtení grafu - 6 bodů
    - Správně načtená metadata - 2 body
    - Správně fungující algoritmus - vzdálenosti - 2 body
    - Správně fungující algoritmus - odkazy pro rekonstrukci - 2 body
    - Za správný seznam stanic na trase - 3 body
    - Správně fungující celý program
        - argument programu z cmd, návratová hodnota main - 2 body
"""


class Vertex:
    """Třída reprezentující vrchol grafu.
    self.id je identifikátor vrcholu.
    self.edges je seznam hran, které vedou z tohoto vrcholu."""

    def __init__(self, id: int) -> None:
        self.id: int = id  # identifikátor uzlu
        self.edges: list[tuple[float, Vertex]] = (
            list()
        )  # (váha hrany, (kam_se_dostanu))


class UndirectedGraph:
    """
    Třída reprezentující neorientovaný graf pomocí seznamu sousednosti.
    Pro uložení uzlů i hran použijte třídu Vertex.
    self.nodes použijte pro uložení všech uzlů v grafu: Neměňte jméno ani typ proměnných!!!
    Správně ji inicializujte v konstruktoru a použijte v metodách __add_node a __add_edge.
    """

    def __init__(self) -> None:
        self.nodes: dict[int, Vertex] = dict()

    def __add_node(self, node: Vertex):
        """Metoda přidá node do grafu.
        Args:
            node (Vertex): uzel, který se má přidat do grafu
        """
        # // TODO Implementujte metodu dle specifikace
        self.nodes[node.id] = node

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

    def create_node(self, id: int) -> Vertex:
        n = Vertex(id)
        self.__add_node(n)
        return n

    def create_edge(self, src_id: int, dst_id: int, weight: float = 0):
        """Metoda přidá hranu do grafu. Vstupují identifikátory uzlů. Pokud uzly neexistují, vytvoří je.
        Interně volá metody __add_node a __add_edge.

        Args:
            src_id (int): Identifikátor uzlu, ze kterého hrana vede.
            dst_id (int): Identifikátor uzlu, do kterého hrana vede.
            weight (float, optional): Ohodnocení hrany. Defaults to 0.
        """
        # // TODO Implementujte metodu dle specifikace
        src = self.nodes.get(src_id, None)
        dst = self.nodes.get(dst_id, None)

        if src is None:
            src = self.create_node(src_id)

        if dst is None:
            dst = self.create_node(dst_id)

        self.__add_edge(src, dst, weight)


# Neměňte signaturu funkce. Dodržte typ návratové hodnoty.
def load_metadata(filename: str) -> dict[str, int]:
    """Načte soubor s uzly a vrátí slovník, kde klíčem je zeměpisné jméno stanice a hodnotou
    je identifikátor vrcholu.

    Args:
        filename (str): Cesta k souboru

    Returns:
        Dict[str, int]: Klíčem je zeměpisné jméno, tedy například 'Vimperk'
        hodnota je identifikátor vrcholu.
    """
    node_dict = dict()
    # TODO Implementujte funkci dle specifikace
    return node_dict


def load_graph(edge_filepath: str) -> UndirectedGraph:
    """Načte graf ze souboru s hranami. Vstupní soubor obsahuje informace o hranách grafu. Pro přesný
    formát se řiďte hlavičkou v poskytnutém souboru a popisem dat na začátku tohoto zdrojového kódu.
    Pro načtení grafu použijte metodu create_edge objektu UndirectedGraph.
    Případné vadné záznamy přeskočte (špatný počet záznamů na řádku, špatný datový typ).

    Args:
        edge_filepath (str): Cesta k souboru s hranami

    Returns:
        UndirectedGraph: Instance třídy UndirectedGraph
    """

    graph = UndirectedGraph()
    # TODO Implementaci funkci dle specifikace
    return graph


def find_solution(
    graph: UndirectedGraph, start_id: int, end_id: int
) -> tuple[dict[int, float], dict[int, int]]:
    """
    Args:
        graph (UndirectedGraph): Instance třídy UndirectedGraph - načtená data.
        start_id (int): Id uzlu, ze kterého cestu hledáme
        end_id (int): Id uzlu, do kterého cestu hledáme

    Returns:
        tuple[dict[int, float], dict[int, int]]:
            Na první pozici je slovník vzdáleností od startu, které se během prohledávání vyčíslily.
                klíč je identifikátor uzlu id (typ int)
                hodnota je nejkratší vzdálenost od startovního vrcholu (typ float)
            Na druhé pozici je slovník, který ukazuje pro uzly, které se během hledání cesty objevily, směr nejkratší cesty ke startu.
                Slouží pro rekonstrukci cesty.
                Klíč je identifikátor uzlu id (typ int), hodnota je id uzlu, ze kterého byla cesta do uzlu nalezena (typ int)

    """
    distances: dict[int, float] = dict()
    predecessors: dict[int, int] = dict()

    return distances, predecessors


def get_list_of_stations(
    predecessors: dict[int, int], nodes_metadata: dict[str, int], end_id: int
) -> list[str]:
    """Vrátí seznam jmen stanic, které jsou na nejkratší cestě mezi startovní a cílovou stanicí. Projde od cílové stanice zpětné ukazatele v slovníku predecessors až k startovní stanici. Všechna jména stanice (ne průjezdné body) vrátí jako seznam ve správném pořadí.
    Od startovní stanice po cílovou - První prvek seznamu je startovní stanice, poslední prvek je cílová stanice.

    Args:
        predecessors (dict[int, int]): výstup z funkce find_solution
        nodes_metadata (dict[str, int]): výstup z funkce load_metadata
        end_id int: cílový uzel

    Returns:
        list[str]: seznam jmen zastávek na trase např. : ["Ceske Budejovice hi nadrazni", "Nove Hodejovice", ..., "Bohumilice v Cechach", "Vimperk"]
    """
    path: list[str] = list()
    current_id = end_id

    while current_id in predecessors:
        node_name = list(nodes_metadata.keys())[
            list(nodes_metadata.values()).index(current_id)
        ]
        path.insert(0, node_name)
        current_id = predecessors[current_id]

    return path


def main(data_path: str) -> list[str]:
    edges_filepath = ""
    nodes_filepath = ""

    graph = load_graph(edges_filepath)  # načte graf
    nodes = load_metadata(nodes_filepath)  # načte metadata o uzlech

    # takto tedy například získáte identifikátory, pro vyhledání řešení
    start = nodes["Ceske Budejovice hi nadrazni"]
    end = nodes["Vimperk"]

    predecessors = None
    distances = None

    find_solution(graph, start_id=start, end_id=end)  # nalezneme řešení

    # Cesta by měla vést z Českých Budějovic a končit ve Vimperku
    # ["Ceske Budejovice hi nadrazni", "Nove Hodejovice", ..., "Bohumilice v Cechach", "Vimperk"]
    path = get_list_of_stations(predecessors, nodes, end)

    return path  # Pro validaci výsledku


if __name__ == "__main__":
    # Program přijímá cestu ke složce s daty. Bude spouštěn následujícím příkazem "python main.py some/path_to/data/folder"
    # TODO implementujte zpracování argumentu z příkazové řádky.
    data_path = ""
    main(data_path)
