import graphviz
import random


class Node:

    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right


def pre_order_traversal(root):
    if root is not None:
        print(root.data, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def in_order_traversal(root):
    if root is not None:
        pre_order_traversal(root.left)
        print(root.data, end=" ")
        pre_order_traversal(root.right)


def generate_unbalanced_tree(depth, values):
    if depth == 0 or not values:
        return None
    value = values.pop(0)
    left_depth = random.randint(0, depth - 1)
    right_depth = depth - 1 - left_depth
    return Node(value, generate_unbalanced_tree(left_depth, values), generate_unbalanced_tree(right_depth, values))


def generate_balanced_tree(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = Node(nums[mid])
    root.left = generate_balanced_tree(nums[:mid])
    root.right = generate_balanced_tree(nums[mid + 1:])

    return root


def bfs(root, value):
    if root is None:
        return []
    queue = [root]
    visited = []
    while queue:
        node = queue.pop(0)
        visited.append(node.data)
        if node.data == value:
            return visited
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


def dfs(root, value):
    if root is None:
        return []
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node.data)
        if node.data == value:
            return visited
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return None


def graphviz_tree(node):
    graph = graphviz.Digraph()
    add_node(graph, node)
    return graph


def add_node(graph, node):
    if node is None:
        return
    graph.node(str(node.data))
    if node.left:
        graph.edge(str(node.data), str(node.left.data))
        add_node(graph, node.left)
    if node.right:
        graph.edge(str(node.data), str(node.right.data))
        add_node(graph, node.right)
