import numpy as np

from node import generate_balanced_tree, generate_unbalanced_tree, pre_order_traversal, bfs, dfs, in_order_traversal
from node import graphviz_tree, is_unbalanced
import time
from prettytable import PrettyTable
from matplotlib import pyplot as plt

import random

if __name__ == "__main__":

    random.seed(140)
    node = 5
    digit_num = 18
    # 16, 15, 35, 58
    depth = 15
    image_num = 0
    arr = [random.randint(1, 150) for i in range(depth)]

    times = list()

    print("Tree number node: ", arr)
    rand = [random.randint(0, len(arr)) for i in range(node)]
    print("Chosen nodes: ", rand)

    temp_arr = list()
    specific_list = list()
    for i in arr:
        temp_arr.append(i)

    for i in rand:
        specific_list.append(arr[i])

    tree1 = generate_balanced_tree(arr)
    print("Balanced tree: ", end='')
    pre_order_traversal(tree1)
    print("")
    tree2 = generate_unbalanced_tree(depth, temp_arr)
    print("Unbalanced tree: ", end='')
    pre_order_traversal(tree2)
    print("")

    # Bfs, balanced

    current_times = list()

    for i in range(len(rand)):
        start_time = time.perf_counter()
        bfs = (tree1, arr[rand[i]])
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times.append(round(time_taken, digit_num))
    times.append(current_times)

    # Bfs, unbalanced

    current_times = list()

    for i in range(len(rand)):
        start_time = time.perf_counter()
        bfs = (tree2, arr[rand[i]])
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times.append(round(time_taken, digit_num))
    times.append(current_times)

    # Dfs, balanced

    current_times = list()

    for i in range(len(rand)):
        start_time = time.perf_counter()
        dfs = (tree1, arr[rand[i]])
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times.append(round(time_taken, digit_num))
    times.append(current_times)

    # Dfs, unbalanced

    current_times = list()

    for i in range(len(rand)):
        start_time = time.perf_counter()
        dfs = (tree2, arr[rand[i]])
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        current_times.append(round(time_taken, digit_num))
    times.append(current_times)

    myTable = PrettyTable(['Node elements', *specific_list])
    myTable.add_row(["BFS Balanced", *times[0]])
    myTable.add_row(["BFS Unbalanced", *times[1]])
    myTable.add_row(["DFS Balanced", *times[2]])
    myTable.add_row(["DFS Unbalanced", *times[3]])
    print(myTable)

    for i in range(4):
        print(myTable[i])

    times_avg = [[0 for j in range(len(times[i]))] for i in range(len(times))]

    for i in range(len(times)):
        for j in range(len(times[i])):
            if j == 0:
                times_avg[i][j] = times[i][j]
            else:
                count = 0
                for z in range(j):
                    count = count + times[i][z]
                times_avg[i][j] = count / (j + 1)

    myTable = PrettyTable(['Nr of nodes', *[i for i in range(1, 6)]])
    myTable.add_row(["BFS Balanced", *times_avg[0]])
    myTable.add_row(["BFS Unbalanced", *times_avg[1]])
    myTable.add_row(["DFS Balanced", *times_avg[2]])
    myTable.add_row(["DFS Unbalanced", *times_avg[3]])
    print(myTable)

    for i in range(4):
        print(myTable[i])

    graph = graphviz_tree(tree1)
    graph.render('balanced_binary_tree.gv', view=True)

    graph = graphviz_tree(tree2)
    graph.render('unbalanced_binary_tree.gv', view=True)

    print("Tree1: ", is_unbalanced(tree1))
    print("Tree2: ", is_unbalanced(tree2))
    print(times_avg)
    nums = [i for i in range(1, 6)]
    x = np.arange(1, len(nums)+1)
    plt.figure(image_num)
    plt.bar(x, times_avg[0], 0.5, label='BFS balanced', color='blue')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('BFS balanced')
    plt.legend()
    image_num += 1

    plt.figure(image_num)
    plt.bar(x, times_avg[1], 0.5, label='BFS unbalanced', color='orange')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('BFS unbalanced')
    plt.legend()
    image_num += 1

    plt.figure(image_num)
    plt.bar(x, times_avg[2], 0.5, label='DFS balanced', color='blue')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('DFS balanced')
    plt.legend()
    image_num += 1

    plt.figure(image_num)
    plt.bar(x, times_avg[3], 0.5, label='DFS unbalanced', color='orange')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('DFS unbalanced')
    plt.legend()
    image_num += 1

    plt.figure(image_num)
    plt.bar(x-0.2, times_avg[0], 0.5, label='BFS balanced', color='orange')
    plt.bar(x+0.2, times_avg[2], 0.5, label='DFS balanced', color='green')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('DFS & BFS balanced')
    plt.legend()
    image_num += 1

    plt.figure(image_num)
    plt.bar(x-0.2, times_avg[1], 0.5, label='BFS unbalanced', color='orange')
    plt.bar(x+0.2, times_avg[3], 0.5, label='DFS unbalanced', color='green')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('DFS & BFS unbalanced')
    plt.legend()
    image_num += 1

    plt.figure(image_num)
    plt.bar(x-0.2, times_avg[0], 0.3, label='BFS balanced', color='orange')
    plt.bar(x-0.1, times_avg[1], 0.3, label='BFS unbalanced', color='cyan')
    plt.bar(x+0.1, times_avg[2], 0.3, label='DFS balanced', color='green')
    plt.bar(x+0.2, times_avg[3], 0.3, label='DFS unbalanced', color='blue')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('Graph search')
    plt.legend()
    plt.show()

