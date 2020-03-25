import Prog_LinkedListUtil as util


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        curr = self.head

        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print()

    def reverseList(self):
        curr = self.head
        prev = None

        while curr:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
        self.head = prev

    def reverse(self, head):
        curr = head
        prev = None

        while curr:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
        # head = prev
        # return head
        return prev


'''
def getNodes():
    """Build custom value linked list node"""
    nodes = []
    n = int(input("Please enter the size of linked list \n"))
    nodes[:n] = []
    # nodes[:n:-1] = []
    i = 1

    while i <= n:
        print(f"Please enter {i} node value: ")
        x = int(input())
        nodes.append(x)
        # nodes[-1*i] = x
        i = i + 1
    # Reverse list or use nodes.insert(0, x) to insert at first position which shifts the nodes towards its right
    reversenodes = nodes[::-1]
    """ print(nodes)
    print(reversenodes) """
    return reversenodes
'''

if __name__ == '__main__':
    """Main method"""
    # nodes = getNodes()
    nodes = util.getNodes()

    ll = LinkedList()

    for node in nodes:
        ll.push(node)

    ll.printList()
    # ll.reverseList()
    ll.head = ll.reverse(ll.head)
    ll.printList()
