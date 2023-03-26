from node import Node, isBalanced, buildTree, printLevelOrder, pre_order_traversal, pre_order_search


class BinaryTree:

    def __init__(self):
        self.root = None

    def add_node(self, data):
        new_node = Node(data)
        # If root is None, assign the new node to the root
        if self.root is None:
            self.root = new_node
        else:
            focus_node = self.root
            parent = None
            while True:
                parent = focus_node
                # If data is less than focus_node, assign focus_node to the left child
                if data < focus_node.data:
                    focus_node = focus_node.left
                    # If there's no left child, assign the new node to the left child
                    if focus_node is None:
                        parent.left = new_node
                        return
                else:
                    focus_node = focus_node.right
                    # If there's no right child, assign the new node to the right child
                    if focus_node is None:
                        parent.right = new_node
                        return

    def pre_order_traversal(self):
        print("Dfs traversal")
        pre_order_traversal(self.root)

    def bfs_traversal(self):
        print("Bfs traversal")
        printLevelOrder(self.root)

    def pre_order_search(self, value):
        print("\nDfs search")
        pre_order_search(self.root, value)

    def isBalanced(self):
        if isBalanced(self.root):
            print("\nBalanced")
        else:
            print("\nUnbalanced")

    def balanced_binary_tree(self):
        print("Balancing the tree")
        self.root = buildTree(self.root)

