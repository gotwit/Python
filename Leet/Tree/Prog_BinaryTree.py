""" try:
    import sys, os
    sys.path.append(os.getcwd())

    from Utils import Prog_Utils as u
except Exception as e:
    print("Exception: ", e) """

class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



class Tree:
    # def __init__(self):
    #     pass

    def build(self, lst, root: Node, i, n) -> Node:
        if i < n:
            temp = Node(lst[i])
            root = temp

            root.left = self.build(lst, root.left, (2 * i + 1), n)
            root.right = self.build(lst, root.right, (2 * i + 2), n)
        return root

    def getHeightOrDepth(self, root: Node) -> int:
        if root is None:
            return 0
        else:
            left_height = self.getHeightOrDepth(root.left)
            right_height = self.getHeightOrDepth(root.right)
        return max(left_height, right_height) + 1

    def bfs(self, root: Node):
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

    def levelOrderTraversal(self, root: Node):
        if root is None:
            return

        nodes = []
        que = Queue()
        que.put(root)

        while not que.empty():
            node = que.queue[0]

            if node:
                nodes.append(node.value)
            else:
                nodes.append(node)
            que.get()

            if node.left and node.right:
                que.put(node.left)
                que.put(node.right)

            # if node.left is None or node.right is None:
            #     if node.left:
            #         que.put(node.left)
            #         que.put(None)
            #     if node.right:
            #         que.put(None)
            #         que.put(node.right)
        return nodes
    
    def inOrderTraversal(self, root: Node):
        stack = []
        nodes = []
        current = root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
        
            elif len(stack) > 0:
                current = stack.pop()
                # print(current.val, end = " ")
                nodes.append(current.val)
                current = current.right
            else:
                break
        # print('\n')
        return nodes

    
    """ def build(self, lst) -> Node:
        i = 0
        n = len(lst)

        node = Node(lst[0])

        while i < n//2:
            node = Node(lst[i])
            node.left = Node(lst[2 * i + 1])
            node.right = Node(lst[2 * i + 2])
            i = i + 1
        return node """