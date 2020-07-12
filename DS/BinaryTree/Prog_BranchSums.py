class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def __init__(self):
        self.totalSum = []
        self.nodes = []
    
    def branchSum(self, root: Node):
        if root is None:
            return
                
        self.nodes.append(root.val)
        self.branchSum(root.left)
        self.branchSum(root.right)
        if root.left is None and root.right is None:
            self.totalSum.append(sum(self.nodes))
        self.nodes.pop()
        return self.totalSum

# O(n) time | O(n) space - where n is the number of nodes in Binary Tree
class Solution2:
    def branchSum(self, root: Node):
        sums = []
        self.calculateBranchSums(root, 0, sums)
        return sums

    def calculateBranchSums(self, root: Node, runningSum, sums):
        if root is None:
            return
        
        newRunningSum = runningSum + root.val
        if root.left is None and root.right is None:
            sums.append(newRunningSum)
            return

        self.calculateBranchSums(root.left, newRunningSum, sums)
        self.calculateBranchSums(root.right, newRunningSum, sums)
        

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
    tree.left.right.left = Node(10)

    sln1 = Solution1()
    result = sln1.branchSum(tree)
    print(f"Solution #1 Branch sum: {result}\n")

    sln2 = Solution2()
    result = sln2.branchSum(tree)
    print(f"Solution #2 Branch sum: {result}\n")