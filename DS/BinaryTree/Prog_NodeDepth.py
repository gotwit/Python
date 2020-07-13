class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution1:
    def __init__(self):
        self.depth = []
    
    def findDepth(self, root: Node, depth):
        depths = []
        self.calculateNodeDepth(root, 0, depths)
        return sum(depths)

    def calculateNodeDepth(self, root: Node, runningDepth, depths):
        if root is None:
            return

        newDepth = runningDepth + 1
        if root.left is not None and root.right is not None:
            depths.append(newDepth-1)
        if root.left is None and root.right is None:
            # depths.append(newDepth-1)
            depths.append(runningDepth)
            return

        self.calculateNodeDepth(root.left, newDepth, depths)
        self.calculateNodeDepth(root.right, newDepth, depths)

class Solution2:
    def nodeDepths(self, root: Node):
        sumOfDepths = 0
        stack = [{"node": root, "depth": 0}]

        while len(stack) > 0:
            nodeInfo = stack.pop()
            node, depth = nodeInfo["node"], nodeInfo["depth"]

            if node is None:
                continue

            sumOfDepths += depth
            stack.append({"node": node.left, "depth": depth + 1})
            stack.append({"node": node.right, "depth": depth + 1})

        return sumOfDepths

class Solution3:
    def nodeDepths(self, root: Node, depth = 0):
        if root is None:
            return 0
        
        return depth + self.nodeDepths(root.left, depth + 1) + self.nodeDepths(root.right, depth + 1)

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
    result = sln1.findDepth(tree, 0)
    print(f"Solution #1 Node depth: {result}")

    sln2 = Solution2()
    result = sln2.nodeDepths(tree)
    print(f"Solution #2 Node depth: {result}")

    sln3 = Solution3()
    result = sln3.nodeDepths(tree)
    print(f"Solution #3 Node depth: {result}")