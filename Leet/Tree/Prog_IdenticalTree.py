try:
    import os, sys

    sys.path.append(os.getcwd())

    from Utils import Prog_Utils as u
    # from ..Tree.Prog_BinaryTree import Tree, Node
    import Prog_BinaryTree as bt
    from collections import deque #deck or double ended queue
except Exception as e:
    print(f"Exception: {e}")

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Inorder traversal
    def isIdentical(self, s: Node, t: Node):
        if s is None and t is None:
            return True

        if s is not None and t is not None:
            return (s.val == t.val) and self.isIdentical(s.left, t.left) and self.isIdentical(s.right, t.right)

        return False

    
    def isIdenticalByDeque(self, t1: Node, t2: Node):
        if t1 is None and t2 is None:
            return True

        if t1 is None or t2 is None:
            return False
        
        deque1 = deque()
        deque2 = deque()
        deque1.append(t1)
        deque2.append(t2)

        while len(deque1) and len(deque2):
            first = deque1.popleft()
            second = deque2.popleft()

            if first.val != second.val:
                return False

            if first.left is not None and second.left is not None:
                deque1.append(first.left)
                deque2.append(second.left)
            elif first.left or second.left:
                return False
            if first.right is not None and second.right is not None:
                deque1.append(first.right)
                deque2.append(second.right)
            elif first.right or second.right:
                return False
        return True


if __name__ == '__main__':

    binaryTree = bt.Tree()

    tree1 = Node(4)
    tree1.left = Node(1)
    tree1.right = Node(2)

    traversal1 = binaryTree.inOrderTraversal(tree1)
    print(f"Tree 1 traversal : {traversal1}\n")

    tree2 = Node(4)
    tree2.left = Node(1)
    tree2.right = Node(2)

    traversal2 = binaryTree.inOrderTraversal(tree2)
    print(f"Tree 2 traversal : {traversal2}\n")

    sln = Solution()
    result = sln.isIdentical(tree1, tree2)
    strbuilder = f"Tree1 {traversal1} is " + ("identical" if result else "not identical") + f" to Tree2 {traversal2} \n"
    print(strbuilder)


if __name__ == '__main__':

    binaryTree = bt.Tree()

    tree1 = Node(3)
    tree1.left = Node(4)
    tree1.right = Node(5)
    tree1.right.right = Node(6)
    tree1.left.left = Node(1)
    tree1.left.right = Node(2)
    # tree1 = None
    traversal1 = binaryTree.inOrderTraversal(tree1)
    print(f"Tree 1 traversal : {traversal1}\n")

    tree2 = Node(3)
    tree2.left = Node(4)
    tree2.right = Node(5)
    tree2.right.right = Node(7)
    tree2.left.left = Node(1)
    tree2.left.right = Node(2)
    # tree2 = None
    traversal2 = binaryTree.inOrderTraversal(tree2)
    print(f"Tree 2 traversal : {traversal2}\n")

    sln = Solution()
    result = sln.isIdenticalByDeque(tree1, tree2)
    strbuilder = f"Tree1 {traversal1} is " + ("identical" if result else "not identical") + f" to Tree2 {traversal2}"
    print(strbuilder)