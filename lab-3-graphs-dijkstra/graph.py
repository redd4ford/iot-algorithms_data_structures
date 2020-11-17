"""Custom Graph."""
import copy
import sys
import doctest

INT_MAX = sys.maxsize


class Graph:
    """
    custom graph implementation.
        NODES is a set of numbers that represent this graph's vertices;
        EDGES is a dictionary where a key is a node and a value is a set
            of neighbour nodes;
        DISTANCES is a dictionary where a key is a pair of two connected
            nodes and a value is a distance between them.
    """

    def __init__(self) -> None:
        """
        init.
        """
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def _add_node(self, node: int) -> None:
        """
        add node to the set of nodes.
        :param node: the node's number to be stored
        :return: none
        >>> graph = Graph()
        >>> graph.add_edge(1, 2, 10)
        >>> print(graph.nodes)
        {1, 2}
        """
        self.nodes.add(node)

    def add_edge(self, from_node: int, to_node: int, distance=INT_MAX) -> None:
        """
        add an edge between two nodes.
        :param from_node: the first node
        :param to_node: the second node
        :param distance: the distance between two nodes
        :return: none
        >>> graph = Graph()
        >>> graph.add_edge(1, 5, 10)
        >>> graph.add_edge(5, 1, 10)
        >>> print(graph.distances)
        {(1, 5): 10, (5, 1): 10}
        """
        self._add_node(from_node)
        self._add_node(to_node)
        self.edges.setdefault(from_node, set()).add(to_node)
        self.distances[from_node, to_node] = distance

    def dijkstra(self, current_node: int) -> dict:
        """
        pick the closest to current_node unchecked vertex, calculate
        the shortest path from current_node to it, and store the distance
        length to distances_to_nodes.
        :param current_node: node, relative to which the lengths of paths
        to other nodes are calculated
        :return distances_to_nodes: a dictionary where a key is a graph's
        node and a value is a distance of the path from current_node to
        this node
        >>> graph = Graph()
        >>> graph.add_edge(1, 2, 20)
        >>> graph.add_edge(2, 1, 20)
        >>> graph.add_edge(1, 4, 25)
        >>> graph.add_edge(4, 1, 25)
        >>> graph.add_edge(2, 3, 20)
        >>> graph.add_edge(3, 2, 20)
        >>> print(graph.dijkstra(2))
        {2: 0, 1: 20, 3: 20, 4: 45}
        """
        max_distance_length = INT_MAX
        distances_to_nodes = {current_node: 0}
        unchecked_nodes = copy.deepcopy(self.nodes)

        while unchecked_nodes:

            closest_node = INT_MAX

            for node in distances_to_nodes:
                if node in unchecked_nodes and node < closest_node:
                    closest_node = node
                    break
            unchecked_nodes.remove(closest_node)

            for neighbour_node in self.edges[closest_node]:
                distance_to_closest_node = distances_to_nodes.get(closest_node) +\
                                                  self.distances[closest_node, neighbour_node]
                if neighbour_node not in distances_to_nodes.keys() or\
                        (distances_to_nodes[neighbour_node] > distance_to_closest_node and
                         max_distance_length >= distance_to_closest_node):
                    distances_to_nodes[neighbour_node] = distance_to_closest_node

        return distances_to_nodes
