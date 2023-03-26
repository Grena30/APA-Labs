class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order_traversal(root):
    if root is not None:
        print(root.data, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def pre_order_search(root, value):
    if root is not None:
        if root.data != value:
            pre_order_search(root.left, value)
            pre_order_search(root.right, value)
        else:
            print(value)


def isBalanced(root):
    # Base condition
    if root is None:
        return True

    # Compute height of left subtree
    lh = isBalanced(root.left)

    # If left subtree is not balanced,
    # return 0
    if lh == 0:
        return 0

    # Do same thing for the right subtree
    rh = isBalanced(root.right)
    if rh == 0:
        return 0

    # Allowed values for (lh - rh) are 1, -1, 0
    if abs(lh - rh) > 1:
        return 0

    # If we reach here means tree is
    # height-balanced tree, return height
    # in this case
    else:
        return max(lh, rh) + 1


def storeBSTNodes(root, nodes):
    # Base case
    if not root:
        return

    # Store nodes in Inorder (which is sorted
    # order for BST)
    storeBSTNodes(root.left, nodes)
    nodes.append(root)
    storeBSTNodes(root.right, nodes)


# Recursive function to construct binary tree
def buildTreeUtil(nodes, start, end):
    # base case
    if start > end:
        return None

    # Get the middle element and make it root
    mid = (start + end) // 2
    node = nodes[mid]

    # Using index in Inorder traversal, construct
    # left and right subtrees
    node.left = buildTreeUtil(nodes, start, mid - 1)
    node.right = buildTreeUtil(nodes, mid + 1, end)
    return node


# This functions converts an unbalanced BST to
# a balanced BST
def buildTree(root):
    # Store nodes of given BST in sorted order
    nodes = []
    storeBSTNodes(root, nodes)

    # Constructs BST from nodes[]
    n = len(nodes)
    return buildTreeUtil(nodes, 0, n - 1)


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i)


# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lh = height(node.left)
        rh = height(node.right)

        # Use the larger one
        if lh > rh:
            return lh + 1
        else:
            return rh + 1
