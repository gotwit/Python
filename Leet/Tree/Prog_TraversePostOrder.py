class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.nodes = []
    # Left subtree, Right subtree, Root node
    def recursivePostOrder(self, root: Node):
        if root is None:
            return

        self.recursivePostOrder(root.left)
        self.recursivePostOrder(root.right)
        self.nodes.append(root.val)

        return self.nodes

if __name__ == "__main__":
    tree1 = Node(3)
    tree1.left = Node(4)
    tree1.right = Node(5)
    tree1.left.left = Node(1)
    tree1.left.right = Node(2)
    tree1.left.right.left = Node(0)

    
    sln = Solution()
    result = sln.recursivePostOrder(tree1)
    print(f"Recursive Post-order traversal: {result}")