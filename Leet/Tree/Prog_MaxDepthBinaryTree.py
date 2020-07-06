try:
    import os, sys

    sys.path.append(os.getcwd())
    
    from Utils import Prog_Utils as u
    # from ..Tree import Prog_BinaryTree as bt
    import Prog_BinaryTree as bt
except Exception as e:
    print(f"Exception: {e}")

""" class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Node)  -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1 """

""" if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.right.left = Node(5)
    root.left.right.right = Node(6)

    sln = Solution()
    depth = sln.maxDepth(root)

    print(f"Max depth of a tree: {depth}") """

if __name__ == '__main__':
    lst = u.getIntList()
    n = len(lst)
    root = None

    binaryTree = bt.Tree()
    tree = binaryTree.build(lst, root, 0, n)
    depth = binaryTree.getHeightOrDepth(tree)
    
    print(depth)