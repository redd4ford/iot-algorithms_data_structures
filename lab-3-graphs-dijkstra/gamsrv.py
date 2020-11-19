"""GAMSRV problem solution."""
import doctest
from graph import Graph, INT_MAX


def get_min_latency(graph: Graph, clients: list) -> int:
    """
    using Dijkstra's algorithm, get latencies from each Router to all nodes.
    find the max latency between the Router and all the Clients. if the max
    latency is minimal, this Router can be considered a good position
    for the Server.
    :param graph: a Graph object
    :param clients: list of numbers of nodes that are Clients (and cannot be
    treated as Routers)
    :return min_path_length: the minimum value of the greatest latency
    to the Client
    >>> graph = Graph()
    >>> graph.add_two_sided_edge(1, 2, 20)
    >>> graph.add_two_sided_edge(1, 4, 25)
    >>> graph.add_two_sided_edge(2, 3, 20)
    >>> graph.add_two_sided_edge(3, 4, 10)
    >>> graph.add_two_sided_edge(4, 6, 60)
    >>> graph.add_two_sided_edge(3, 5, 30)
    >>> graph.add_two_sided_edge(5, 6, 10)
    >>> clients = [1, 3, 6]
    >>> print(get_min_latency(graph, clients))
    50
    """
    min_path_length = INT_MAX

    for current_node in range(1, len(graph.nodes) + 1):
        if current_node not in clients:
            max_path_length = 0
            paths_to_all_nodes = graph.dijkstra(current_node)

            for client_node in clients:
                if max_path_length < paths_to_all_nodes[client_node]:
                    max_path_length = paths_to_all_nodes[client_node]

            if min_path_length > max_path_length:
                min_path_length = max_path_length
    return min_path_length


def main(IN_FILE='gamsrv.in', OUT_FILE='gamsrv.out') -> None:
    """
    get the total number of nodes, number of client nodes, and edges from
    .in file. then, find the Server location that minimizes the largest latency
    value to the Client.
    :return: none
    >>> main('examples/1.in', 'examples/1.out')
    >>> with open('examples/1.out', 'r') as file: print(file.readline())
    100
    >>> main('examples/2.in', 'examples/2.out')
    >>> with open('examples/2.out', 'r') as file: print(file.readline())
    10
    >>> main('examples/3.in', 'examples/3.out')
    >>> with open('examples/3.out', 'r') as file: print(file.readline())
    1000000000
    """
    graph = Graph()
    with open(IN_FILE, 'r') as in_file:
        file_data = in_file.readlines()

    clients = list(map(int, file_data[1].split(' ')))
    # at this point edges contains lines of raw data: 'start_node end_node latency\n'
    edges = file_data[2:]

    for edge in edges:
        # 'unpacking' edges
        start_node, end_node, latency = list(map(int, edge.split(' ')))
        graph.add_two_sided_edge(start_node, end_node, latency)

    min_path_length = get_min_latency(graph, clients)

    open(OUT_FILE, 'w').write(str(min_path_length))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    main()
