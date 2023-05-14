from algorithms import *
import time
import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable
import random
import math

random.seed(105)
nodes = [10, 25, 70, 500, 3000, 6000, 11000, 25000, 70000, 150000, 200000]
digit = 5
graphs = []
times_p = []
times_k =[]
mst_p = []
mst_k = []
image_num = 1

# Example

gE = generate_random_graph(10, 11)
draw_graph(gE, 'Example Graph')

p = prim(gE)
k = kruskal(gE)
print(p)
print(k)

gP = generate_mst_graph(gE, p)
gK = generate_mst_graph(gE, k)
draw_graph(gP, 'Prim MST')
draw_graph(gK, 'Kruskal MST')

# Nodes

for i in nodes:
    graph = generate_random_graph(i, 2*i)
    graphs.append(graph)

    start_time = time.perf_counter()
    p = prim(graph)
    end_time = time.perf_counter()
    times_p.append(round((end_time - start_time), digit))
    mst_p.append(p)

    start_time = time.perf_counter()
    k = kruskal(graph)
    end_time = time.perf_counter()
    times_k.append(round((end_time - start_time), digit))
    mst_k.append(k)

# Tables

mst = 'MST computation graph time: ' + str(nodes) + ' (s)'

myTable = PrettyTable(['Minimal Spanning Tree', *[mst]])
myTable.add_row(["Prim algorithm", *[times_p]])
myTable.add_row(["Kruskal algorithm", *[times_k]])
print(myTable)

for i in myTable:
    print(i)

# Graphs

plt.figure(image_num)
plt.plot(nodes, times_p, label='Prim', color='orange')
plt.xlabel('Graph nodes')
plt.ylabel('MST computation time, s')
plt.title('Prim algorithm')
plt.legend()
image_num += 1

plt.figure(image_num)
plt.plot(nodes, times_k, label='Kruskal', color='blue')
plt.xlabel('Graph nodes')
plt.ylabel('MST computation time, s')
plt.title('Kruskal algorithm')
plt.legend()
image_num += 1

plt.figure(image_num)
plt.plot(nodes, times_p, label='Prim', color='orange')
plt.plot(nodes, times_k, label='Kruskal', color='blue')
plt.xlabel('Graph nodes')
plt.ylabel('MST computation time, s')
plt.title('MST algorithms')
plt.legend()
image_num += 1

plt.show()