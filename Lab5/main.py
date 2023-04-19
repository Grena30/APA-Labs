import random
from graph import generate_random_graph, draw_graph, floyd, dijkstra
import time


random.seed(100)

times = list()
nodes = [10, 25, 50, 100, 1000]
graphs = list()

# 5-7 (100), 15-12 (100), 30-30 (100)
graph = generate_random_graph(15, 25)

shortest_path_dj = dijkstra(graph, '1', '7')
shortest_path_f = floyd(graph, '1', '7')
print(shortest_path_dj)
print(shortest_path_f)


for i in nodes:
    # sparse
    graph_a = generate_random_graph(i, i/2)
    start_time = time.perf_counter()
    end_time = time.perf_counter()

    # dense
    graph_b = generate_random_graph(i, 2*i)


