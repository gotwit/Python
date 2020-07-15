class Node:
    def __init__(self, value = None, parent = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def callback(lst, tree:Node):
    if tree is None:
        return
    lst.append(tree.value)

# O(n) time | O(1) space
class Solution1:
    def inOrderTraversal(self, tree: Node, callback):
        previousNode = None
        currentNode = tree

        while currentNode is not None:
            if previousNode is None or previousNode == currentNode.parent:
                if currentNode.left is not None:
                    nextNode = currentNode.left
                else:
                    callback(currentNode)
                    if currentNode.right is not None:
                        nextNode = currentNode.right
                    else:
                        nextNode = currentNode.parent
            elif previousNode == currentNode.left:
                callback(currentNode)
                if currentNode.right is not None:
                    nextNode = currentNode.right
                else:
                    nextNode = currentNode.parent
            elif previousNode == currentNode.right:
                nextNode = currentNode.parent

            previousNode = currentNode
            currentNode = nextNode


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2, parent=tree)
    tree.right = Node(3, parent=tree)
    tree.left.left = Node(4, parent=tree.left)
    tree.left.left.right = Node(9, tree.left.left)
    tree.right.left = Node(6, tree.right)
    tree.right.right = Node(7, tree.right)

    lst = []
    sln1 = Solution1()
    actualCallback = lambda x: callback(lst, x)
    sln1.inOrderTraversal(tree, actualCallback)
    print(f"Solution #1 Inorder tree traversal: {lst}\n")