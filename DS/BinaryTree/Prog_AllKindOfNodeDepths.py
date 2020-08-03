class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
def nodeDepths(root: Node, depth):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

def allKindOfNodeDepths(root, depths):
    depth = calculateDepth(root, depths)
    return depth

def calculateDepth(root, depths):
    if root is None:
        return

    calculateDepth(root.left, depths)
    depth = nodeDepths(root, 0)
    depths.append(depth)
    calculateDepth(root.right, depths)

    return depths

if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.left.left.left = Node(8)
    tree.left.left.right = Node(9)

    result = allKindOfNodeDepths(tree, [])

    print(f"All node depths: {result}")