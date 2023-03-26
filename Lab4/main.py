from binary_tree import BinaryTree
import time

import random

if __name__ == "__main__":

    n = random.randint(15, 45)
    random.seed(110)
    tree = BinaryTree()
    arr = [random.randint(1, 50) for i in range(5000)]
    for i in arr:
        tree.add_node(i)
    tree.pre_order_traversal()
    tree.isBalanced()
    tree.balanced_binary_tree()
    tree.pre_order_traversal()
    tree.isBalanced()
    tree.bfs_traversal()

    start = time.perf_counter()
    tree.pre_order_search(47)
    end = time.perf_counter()
    time = start-end
    print(end)
