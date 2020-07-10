try:
    import os, sys

    sys.path.append(os.getcwd())

    from Utils import Prog_Utils as u
    import Prog_BinaryTree as bt
    import Prog_IdenticalTree as it
except Exception as e:
    print(f"Exception: {e}")

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursiveInOrder(self, root: Node, left: bool):
        if root is None:
            if left:
                return "lNone"
            else:
                return "rNone"

        return self.recursiveInOrder(root.left, True) + " " + "#" + str(root.val) + " " + self.recursiveInOrder(root.right, False)
    
    def recursivePreOrder(self, root: Node, left: bool):
        if root is None:
            if left:
                return "lNone"
            else:
                return "rNone"

        return "#" + str(root.val) + " " + self.recursivePreOrder(root.left, True) + " " + self.recursivePreOrder(root.right, False)

    # Time complexity : O(m^2+n^2+m*n)O(m^2+n^2+m∗n). A total of n nodes of the tree s and m nodes of tree t are traversed. 
    # Assuming string concatenation takes O(k)O(k) time for strings of length kk and indexOf takes O(m*n)O(m∗n).

    # Space complexity : O(max(m,n))O(max(m,n)). The depth of the recursion tree can go upto nn for tree tt and mm for tree ss in worst case.
    def isSubtree1(self, root1: Node, root2: Node):
        inOrdTreeSln1 = Solution()
        preOrdTreeSln1 = Solution()
        inOrdTreeSln2 = Solution()
        preOrdTreeSln2 = Solution()

        inorderTree1 = inOrdTreeSln1.recursiveInOrder(root1, True)
        preOrdTree1 = preOrdTreeSln1.recursivePreOrder(root1, True)
        inorderTree2 = inOrdTreeSln2.recursiveInOrder(root2, True)
        preOrdTree2 = preOrdTreeSln2.recursivePreOrder(root2, True)

        # print(f"Tree 1 inorder traversal : {inorderTree1}\n")
        # print(f"Tree 1 preorder traversal : {preOrdTree1}\n")
        # print(f"Tree 2 inorder traversal : {inorderTree2}\n")
        # print(f"Tree 2 preorder traversal : {preOrdTree2}\n")
        result = inorderTree1.find(inorderTree2) >= 0 and preOrdTree1.find(preOrdTree2) >= 0
        return result

        # Time complexity : O(m*n)O(m∗n). In worst case(skewed tree) traverse function takes O(m*n)O(m∗n) time.
        # Space complexity : O(n). The depth of the recursion tree can go upto n. n refers to the number of nodes in s.

    def equals(self, root1: Node, root2: Node):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        return root1.val == root2.val and self.equals(root1.left, root2.left) and self.equals(root1.right, root2.right)

    def traverse(self, root1: Node, root2: Node):
        return root1 is not None and (self.equals(root1, root2) or self.traverse(root1.left, root2) or self.traverse(root1.right, root2))

    def isSubtree2(self, tree1: Node, tree2: Node):
        return self.traverse(tree1, tree2)


if __name__ == "__main__":
    tree1 = Node(3)
    tree1.left = Node(4)
    tree1.right = Node(5)
    tree1.left.left = Node(1)
    tree1.left.right = Node(2)
    # tree1.left.right.left = Node(0)

    """ inOrdTreeSln1 = inOrdTree.Solution()
    preOrdTreeSln1 = preOrdTree.Solution()

    inorderTree1 = inOrdTreeSln1.recursiveInOrder(tree1)
    print(f"Tree 1 inorder traversal : {inorderTree1}\n")

    preOrdTree1 = preOrdTreeSln1.recursivePreOrder(tree1)
    print(f"Tree 1 preorder traversal : {preOrdTree1}\n") """

    tree2 = Node(4)
    tree2.left = Node(1)
    tree2.right = Node(2)

    """ inOrdTreeSln2 = inOrdTree.Solution()
    preOrdTreeSln2 = preOrdTree.Solution()

    inorderTree2 = inOrdTreeSln2.recursiveInOrder(tree2)
    print(f"Tree 2 inorder traversal : {inorderTree2}\n")

    preOrdTree2 = preOrdTreeSln2.recursivePreOrder(tree2)
    print(f"Tree 2 preorder traversal : {preOrdTree2}\n") """

    sln = Solution()
    result = sln.isSubtree1(tree1, tree2)
    strbuilder = f"Tree1 is " + ("subtree" if result else "not subtree") + f" to Tree2"
    print(strbuilder)

    sln2 = Solution()
    result = sln2.isSubtree2(tree1, tree2)
    strbuilder = f"Tree1 is " + ("subtree" if result else "not subtree") + f" to Tree2"
    print(strbuilder)