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


def draw_graph(graph):
    dot = Digraph()
    added_edges = set()
    for node in graph:
        dot.node(node)
        for neighbor, weight in graph[node].items():
            if (node, neighbor) not in added_edges and (neighbor, node) not in added_edges:
                dot.edge(node, neighbor, label=str(weight), dir='none')
                added_edges.add((node, neighbor))
    dot.render('graph', view=True)


def dijkstra(graph, start, target):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == target:
            return distances[target]

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return -1  # If target is not reachable from start


def floyd(graph, start, target):
    if start not in graph or target not in graph:
        return -1

    dist = {}
    for i in graph:
        dist[i] = {}
        for j in graph:
            if i == j:
                dist[i][j] = 0
            elif i in graph and j in graph[i]:
                dist[i][j] = graph[i][j]
            else:
                dist[i][j] = float('inf')

    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    if dist[start][target] == float('inf'):
        return -1
    else:
        return dist[start][target]

