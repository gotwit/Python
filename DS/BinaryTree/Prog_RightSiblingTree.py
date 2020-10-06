class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(d) where n is no of nodes, space d is the height of tree
# if perfectly balanced tree O(log n) space
def rightSiblingTree(root):
    mutate(root, None, None)
    return root

def mutate(node: Node, parent: Node, isLeftChild = False):
    if node is None:
        return
    left, right = node.left, node.right
    mutate(left, node, True)
    if parent is None:
        node.right = None
    elif isLeftChild:
        node.right = parent.right
    else: # rightChild
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate(right, node, False)