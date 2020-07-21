# Flatten Binary Tree
class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def getNodesInOrder(tree, array):
    if tree is not None:
        getNodesInOrder(tree.left, array)
        array.append(tree)
        getNodesInOrder(tree.right, array)
    return array

# O(n) time | O(n) space
class Solution1:

    def flatten(self, root: Node):
        inOrderNodes = getNodesInOrder(root, [])

        for i in range(0, len(inOrderNodes) - 1):
            leftNode = inOrderNodes[i]
            rightNode = inOrderNodes[i + 1]

            leftNode.right = rightNode
            rightNode.left = leftNode
        return inOrderNodes[0]

# O(n) time | O(d) space depth of the tree in call stack
class Solution2:
    def flatten(self, root: Node):
        leftMost, _ = self.flattenTree(root)
        return leftMost

    def flattenTree(self, node):
        if node.left is None:
            leftMost = node
        else:
            leftSubtreeLeftMost, leftSubtreeRightMost = self.flattenTree(node.left)
            self.connectNodes(leftSubtreeRightMost, node)
            leftMost = leftSubtreeLeftMost
        if node.right is None:
            rightMost = node
        else:
            rightSubtreeLeftMost, rightSubtreeRightMost = self.flattenTree(node.right)
            self.connectNodes(node, rightSubtreeLeftMost)
            rightMost = rightSubtreeRightMost

        return [leftMost, rightMost]

    def connectNodes(self, left, right):
        left.right = right
        right.left = left


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(7)
    tree.left.right.right = Node(8)
    tree.right.left = Node(6)