from queue import Queue

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def bfs(root: Node):
        nodes = []

        if root is None:
            return nodes

        que = Queue()
        que.put(root)

        while not que.empty():
            node = que.queue[0]
            que.get()

            if not node:
                nodes.append(node)
            else:
                nodes.append(node.value)

                if node.left and node.right:
                    que.put(node.left)
                    que.put(node.right)

                if node.left is None or node.right is None:
                    if node.left:
                        que.put(node.left)
                        que.put(None)
                    if node.right:
                        que.put(None)
                        que.put(node.right)
        return nodes

class Solution1:
    def invert(self, root: Node):
        nodes = bfs(root)
        n = len(nodes)
        invertedTree = self.buildTree(nodes, root, 0, n)
        invertedNodes = bfs(invertedTree)
        return invertedNodes

    def buildTree(self, nodes, root: Node, i, n) -> Node:
        if i < n:
            if nodes[i]:
                temp = Node(nodes[i])
                root = temp

                root.left = self.buildTree(nodes, root.left, (2 * i + 2), n)
                root.right = self.buildTree(nodes, root.right, (2 * i + 1), n)
        return root


class Solution2:
    def invert(self, root: Node):
        if root is None:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invert(root.left)
        self.invert(root.right)
        nodes = bfs(root)
        return nodes

# O(n) time | O(n) space
class Solution3:
    def invert(self, tree: Node):
        queue = [tree]

        while len(queue):
            current = queue.pop(0)

            if current is None:
                continue
            self.swapLeftAndRight(current)
            self.invert(tree.left)
            self.invert(tree.right)
        nodes = bfs(tree)
        return nodes

    def swapLeftAndRight(self, tree: Node):
        tree.left, tree.right = tree.right, tree.left

# O(n) time | O(d) space
class Solution4:
    def invert(self, tree: Node):
        if tree is None:
            return
        
        self.swapLeftAndRight(tree)
        self.invert(tree.left)
        self.invert(tree.right)
        nodes = bfs(tree)
        return nodes
        
    def swapLeftAndRight(self, tree: Node):
        tree.left, tree.right = tree.right, tree.left      

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

    sln1 = Solution1()
    result = sln1.invert(tree)
    print(f"Solution #1 Invert Binary Tree: {result}\n")

    tree2 = Node(1)
    tree2.left = Node(2)
    tree2.right = Node(3)
    # tree2.left.left = Node(4)
    tree2.left.right = Node(5)
    # tree2.right.left = Node(6)
    # tree2.right.right = Node(7)
    # tree2.left.left.left = Node(8)
    # tree2.left.left.right = Node(9)

    result2 = sln1.invert(tree2)
    print(f"Solution #2 Invert Binary Tree: {result2}\n")

    tree3 = Node(1)
    tree3.left = Node(2)
    tree3.right = Node(3)
    tree3.left.left = Node(4)
    tree3.left.right = Node(5)
    tree3.right.left = Node(6)
    tree3.right.right = Node(7)
    tree3.left.left.left = Node(8)
    tree3.left.left.right = Node(9)

    sln2 = Solution2()
    result3 = sln2.invert(tree3)
    print(f"Solution #3 Invert Binary Tree: {result3}\n")

    tree4 = Node(1)
    tree4.left = Node(2)
    tree4.right = Node(3)
    tree4.left.right = Node(5)

    result4 = sln2.invert(tree4)
    print(f"Solution #4 Invert Binary Tree: {result4}\n")


    tree5 = Node(1)
    tree5.left = Node(2)
    tree5.right = Node(3)
    tree5.left.left = Node(4)
    tree5.left.right = Node(5)
    tree5.right.left = Node(6)
    tree5.right.right = Node(7)
    tree5.left.left.left = Node(8)
    tree5.left.left.right = Node(9)

    sln3 = Solution3()
    result5 = sln3.invert(tree5)
    print(f"Solution #5 Invert Binary Tree: {result5}\n")

    tree6 = Node(1)
    tree6.left = Node(2)
    tree6.right = Node(3)
    tree6.left.right = Node(5)

    result6 = sln3.invert(tree6)
    print(f"Solution #6 Invert Binary Tree: {result6}\n")

    tree7 = Node(1)
    tree7.left = Node(2)
    tree7.right = Node(3)
    tree7.left.left = Node(4)
    tree7.left.right = Node(5)
    tree7.right.left = Node(6)
    tree7.right.right = Node(7)
    tree7.left.left.left = Node(8)
    tree7.left.left.right = Node(9)

    sln4 = Solution4()
    result7 = sln4.invert(tree7)
    print(f"Solution #7 Invert Binary Tree: {result7}\n")

    tree8 = Node(1)
    tree8.left = Node(2)
    tree8.right = Node(3)
    tree8.left.right = Node(5)

    result8 = sln3.invert(tree8)
    print(f"Solution #8 Invert Binary Tree: {result8}\n")


""" n = len(nodes)
if n > 0:
    i = 0
    temp = Node(nodes[i])
    root = temp
    noOfNodes = n//2
    
    while i < noOfNodes:
        left_node = nodes[(2 * i + 1)]
        right_node = nodes[(2 * i + 2)]
        
        if left_node is not None:
            root.right = Node(left_node)

        if right_node is not None:
            root.left = Node(right_node)
        i += 1
invertedNodes = self.bfs(root)
return invertedNodes """