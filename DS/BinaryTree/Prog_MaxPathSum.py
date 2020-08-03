# O(n) time | O(log(n)) space, where tree is perfectly balanced otherwise O(n)
class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def maxPathSum(tree):
    maxSumAsBranch, runningMaxPathSum = findMaxSum(tree)
    return runningMaxPathSum

def findMaxSum(tree):
    if tree is None:
        return (0, 0)

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)

    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNode = max(maxSumAsBranch, leftMaxSumAsBranch + value + rightMaxSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

    return (maxSumAsBranch, maxPathSum)


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    result = maxPathSum(tree)
    print(f"Max path sum: {result}\n")

    