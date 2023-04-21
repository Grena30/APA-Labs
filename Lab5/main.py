import math
import random

import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable

from graph import generate_sparse_graph, generate_complete_graph, draw_graph, floyd, dijkstra
import time

random.seed(100)

times_floyd = list()
times_dj = list()
nodes = [10, 25, 50, 100]
nodes_searched = list()
node_search = list()
digit_num = 6
image_num = 1

# 5-7 (100), 15-12 (100), 30-30 (100)
graph_sparse = generate_sparse_graph(5, 2 / 5)
graph_dense = generate_complete_graph(5)
draw_graph(graph_sparse, 'sparse_graph')
draw_graph(graph_dense, 'dense_graph')


for i in nodes:

    current_times_dj = list()
    current_times_floyd = list()
    random_nodes = list()
    nodes_searched.append('Graph ' + str(i))
    node_search.append('Graph: ' + str(i))

    # Sparse graph
    nodes_searched.append('Sparse: ')
    node_search.append('Sparse: ')
    graph_sparse = generate_sparse_graph(i, 2 / i)

    if i / 5 >= 5:
        search = 5
    else:
        search = math.floor(i / 5)

    for j in range(search):
        start_node = str(random.randint((j + 1), (j + 1) * 2))
        end_node = str(random.randint((j + 1) * 3, (j + 1) * 5))

        # Dijkstra
        start_time = time.perf_counter()
        shortest_path_dj = dijkstra(graph_sparse, start_node, end_node)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times_dj.append(round(time_taken, digit_num))

        # Floyd

        start_time = time.perf_counter()
        shortest_path_floyd = floyd(graph_sparse, start_node, end_node)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times_floyd.append(round(time_taken, digit_num))

        random_nodes.append([start_node, end_node])
        nodes_searched.append(start_node + '-' + end_node + ' = ' + str(shortest_path_dj) + ' | ')
        node_search.append(start_node + '-' + end_node + ' | ')

    # Dense graph
    nodes_searched.append('Dense: ')
    node_search.append('Dense: ')
    graph_dense = generate_complete_graph(i)

    for j in random_nodes:
        start_node = j[0]
        end_node = j[1]

        # Dijkstra

        start_time = time.perf_counter()
        shortest_path_dj = dijkstra(graph_dense, start_node, end_node)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times_dj.append(round(time_taken, digit_num))

        # Floyd

        start_time = time.perf_counter()
        shortest_path_floyd = floyd(graph_dense, start_node, end_node)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times_floyd.append(round(time_taken, digit_num))

        nodes_searched.append(start_node + '-' + end_node + ' = ' + str(shortest_path_dj) + ' | ')
        node_search.append(start_node + '-' + end_node + ' | ')

    times_floyd.append(current_times_floyd)
    times_dj.append(current_times_dj)

myTable = PrettyTable(['Graphs', *['Sparse graph', 'Dense graph']])
myTable.add_row(["Dijkstra 10 nodes", *[times_dj[0][0:2], times_dj[0][2:4]]])
myTable.add_row(["Floyd 10 nodes", *[times_floyd[0][0:2], times_floyd[0][2:4]]])
myTable.add_row(["Dijkstra 25 nodes", *[times_dj[1][0:5], times_dj[1][5:10]]])
myTable.add_row(["Floyd 25 nodes", *[times_floyd[1][0:5], times_floyd[1][5:10]]])
myTable.add_row(["Dijkstra 50 nodes", *[times_dj[2][0:5], times_dj[2][5:10]]])
myTable.add_row(["Floyd 50 nodes", *[times_floyd[2][0:5], times_floyd[2][5:10]]])
myTable.add_row(["Dijkstra 100 nodes", *[times_dj[3][0:5], times_dj[3][5:10]]])
myTable.add_row(["Floyd 100 nodes", *[times_floyd[3][0:5], times_floyd[3][5:10]]])

print(myTable)

count = 0
for i in nodes_searched:
    if i.__contains__('Graph'):
        print('\n')
        print(i)
    else:
        print(i, end='')
print('\n')

count = 0
for i in node_search:
    if i.__contains__('Graph'):
        print('\n')
        print(i)
    else:
        print(i, end='')
print('\n')

for i in range(4):
    print(myTable[2*i])

for i in range(4):
    print(myTable[2*i+1])


arr = [i for i in range(5)]
x = np.arange(1, len(arr)+1)

# Dijkstra
plt.figure(image_num)
plt.bar(x-0.3, times_dj[1][0:5], 0.2, label='Sparse 25 ', color='cyan')
plt.bar(x-0.2, times_dj[2][0:5], 0.2, label='Sparse 50', color='green')
plt.bar(x-0.1, times_dj[3][5:10], 0.2, label='Sparse 100', color='blue')
plt.bar(x+0.1, times_dj[1][5:10], 0.2, label='Dense 25', color='black')
plt.bar(x+0.2, times_dj[2][5:10], 0.2, label='Dense 50', color='red')
plt.bar(x+0.3, times_dj[3][5:10], 0.2, label='Dense 100', color='orange')
plt.xlabel('Nodes checked')
plt.ylabel('Elapsed time, s')
plt.title('Dijkstra shortest path')
plt.legend()
image_num += 1

# Floyd
plt.figure(image_num)
plt.bar(x-0.3, times_floyd[1][0:5], 0.2, label='Sparse 25 ', color='cyan')
plt.bar(x-0.2, times_floyd[2][0:5], 0.2, label='Sparse 50', color='green')
plt.bar(x-0.1, times_floyd[3][5:10], 0.2, label='Sparse 100', color='blue')
plt.bar(x+0.1, times_floyd[1][5:10], 0.2, label='Dense 25', color='black')
plt.bar(x+0.2, times_floyd[2][5:10], 0.2, label='Dense 50', color='red')
plt.bar(x+0.3, times_floyd[3][5:10], 0.2, label='Dense 100', color='orange')
plt.xlabel('Nodes checked')
plt.ylabel('Elapsed time, s')
plt.title('Floyd shortest path')
plt.legend()
image_num += 1

# Both 50-100
plt.figure(image_num)
plt.bar(x-0.4, times_dj[2][0:5], 0.2, label='Dijkstra sparse 50 ', color='cyan')
plt.bar(x-0.3, times_dj[3][0:5], 0.2, label='Dijkstra sparse 100', color='green')
plt.bar(x-0.2, times_floyd[2][0:5], 0.2, label='Floyd sparse 50', color='blue')
plt.bar(x+0.1, times_floyd[3][0:5], 0.2, label='Floyd sparse 100', color='black')
plt.bar(x+0.1, times_dj[2][5:10], 0.2, label='Dijkstra dense 50', color='red')
plt.bar(x+0.2, times_dj[3][5:10], 0.2, label='Dijkstra dense 100', color='orange')
plt.bar(x+0.3, times_floyd[2][5:10], 0.2, label='Floyd dense 50', color='yellow')
plt.bar(x+0.4, times_floyd[3][5:10], 0.2, label='Floyd dense 100', color='pink')
plt.xlabel('Nodes checked')
plt.ylabel('Elapsed time, s')
plt.title('Shortest path')
plt.legend()
image_num += 1

plt.show()
