"""GAMSRV problem solution."""
import doctest
from graph import Graph, INT_MAX


def main() -> None:
    """
    get the total number of nodes, number of client nodes, and edges from
    .in file. then, for each router, get latencies from it to all the clients.
    find the max latency between the router and all the clients. if the max
    latency is minimal, this router can be considered a good position
    for the server.
    :return: none
    >>> with open('gamsrv.out', 'r') as file: print(file.readline())
    50
    """
    graph = Graph()
    with open('gamsrv.in', 'r') as in_file:
        file_data = in_file.readlines()

    nodes_count = int(file_data[0].split(' ')[0])
    nodes = [node + 1 for node in range(0, nodes_count)]
    clients = list(map(int, file_data[1].split(' ')))
    # at this point edges contains lines of raw data: 'start_node end_node latency\n'
    edges = file_data[2:]

    for edge in edges:
        # 'unpacking' edges
        start_node, end_node, latency = list(map(int, edge.split(' ')))
        graph.add_edge(start_node, end_node, latency)
        graph.add_edge(end_node, start_node, latency)

    min_path_length = INT_MAX

    for current_node in range(1, len(nodes) + 1):
        if current_node not in clients:
            max_path_length = 0
            paths_to_all_nodes = graph.dijkstra(current_node)

            for client_node in clients:
                if max_path_length < paths_to_all_nodes[client_node]:
                    max_path_length = paths_to_all_nodes[client_node]

            if min_path_length > max_path_length:
                min_path_length = max_path_length

    open('gamsrv.out', 'w').write(str(min_path_length))


if __name__ == '__main__':
    # doctest.testmod(verbose=True)
    main()
