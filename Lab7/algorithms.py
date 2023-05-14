import random
from graphviz import Digraph
import heapq


def generate_random_graph(num_nodes, num_edges):
    graph = {str(i): {} for i in range(num_nodes)}
    nodes = list(graph.keys())

    while num_edges > 0:
        u, v = random.sample(nodes, 2)
        if v not in graph[u]:
            weight = random.randint(1, 10)
            graph[u][v] = weight
            graph[v][u] = weight
            num_edges -= 1

    return graph


def draw_graph(graph, string):
    dot = Digraph()
    added_edges = set()
    for node in graph:
        dot.node(node)
        for neighbor, weight in graph[node].items():
            if (node, neighbor) not in added_edges and (neighbor, node) not in added_edges:
                dot.edge(node, neighbor, label=str(weight), dir='none')
                added_edges.add((node, neighbor))
    dot.render(string, view=True)


def generate_complete_graph(num_nodes):
    graph = {str(i): {} for i in range(num_nodes)}
    nodes = list(graph.keys())

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, 10)
            graph[nodes[i]][nodes[j]] = weight
            graph[nodes[j]][nodes[i]] = weight

    return graph


def prim(graph):
    # Initialize the set of vertices to be visited and the minimum spanning tree
    visited = set()
    mst = []
    # Select an arbitrary vertex to start with
    start_vertex = next(iter(graph))
    # Add the starting vertex to the set of visited vertices
    visited.add(start_vertex)
    # Get the edges that are adjacent to the starting vertex and add them to the priority queue
    edges = [
        (cost, start_vertex, end_vertex)
        for end_vertex, cost in graph[start_vertex].items()
    ]
    heapq.heapify(edges)
    # Loop through the priority queue
    while edges:
        # Get the edge with the smallest weight
        cost, start_vertex, end_vertex = heapq.heappop(edges)
        # If the destination vertex has not been visited yet, add the edge to the minimum spanning tree and add the destination vertex to the set of visited vertices
        if end_vertex not in visited:
            visited.add(end_vertex)
            mst.append((start_vertex, end_vertex, cost))
            # Get the edges that are adjacent to the destination vertex and add them to the priority queue
            for next_vertex, cost in graph[end_vertex].items():
                if next_vertex not in visited:
                    heapq.heappush(edges, (cost, end_vertex, next_vertex))
    # Return the minimum spanning tree
    return mst


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)
        if i_root == j_root:
            return False
        if self.rank[i_root] > self.rank[j_root]:
            self.parent[j_root] = i_root
        else:
            self.parent[i_root] = j_root
            if self.rank[i_root] == self.rank[j_root]:
                self.rank[j_root] += 1
        return True


def kruskal(graph):
    # Initialize the minimum spanning tree and the disjoint set
    mst = []
    ds = DisjointSet(len(graph))
    # Get the edges and sort them by weight
    edges = [(cost, start_vertex, end_vertex) for start_vertex, edges in graph.items() for end_vertex, cost in
             edges.items()]
    edges.sort()
    # Loop through the edges and add them to the minimum spanning tree if they don't create a cycle
    for cost, start_vertex, end_vertex in edges:
        if ds.union(int(start_vertex), int(end_vertex)):
            mst.append((start_vertex, end_vertex, cost))
    # Return the minimum spanning tree
    return mst


def generate_mst_graph(graph, mst):
    mst_graph = {node: {} for node in graph}
    for edge in mst:
        start_vertex, end_vertex, weight = edge
        mst_graph[start_vertex][end_vertex] = weight
        mst_graph[end_vertex][start_vertex] = weight
    return mst_graph




