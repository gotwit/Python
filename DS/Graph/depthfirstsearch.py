class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def depthfirstsearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthfirstsearch(array)
        return array

    def printGraph(self, arr):
        for node in arr:
            print(node, end=' ')
        print()


graph = Node("A")
graph.addChild("B")
graph.addChild("C")
graph.addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")

array = graph.depthfirstsearch([])
graph.printGraph(array)
