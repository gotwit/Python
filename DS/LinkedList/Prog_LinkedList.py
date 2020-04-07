import LinkedList.Prog_LinkedListUtil as util


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    '''Single Linked List'''

    # Initialize the head pointer
    def __init__(self):
        self.head = None

    # Add a node at the front
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    # Add a node after a given node
    def insertAfter(self, prev_node, value):
        if prev_node is None:
            print(f"Node {prev_node.value} doesn't exist\n")
            return

        newNode = Node(value)
        newNode.next = prev_node.next
        prev_node.next = newNode

    # Add a node at the end
    def append(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return

        # Traverse the list till last node
        last = self.head

        while last.next:
            last = last.next
        last.next = newNode

    # Print node value
    def printList(self):
        curr = self.head

        while curr is not None:
            print(curr.value, end=" ")
            curr = curr.next
        print()


if __name__ == "__main__":
    # Don't use util.getNodes it reverse the user input values by default
    # nodes = util.getNodes()

    ll = LinkedList()
    ll.push(10)
    ll.insertAfter(ll.head, 20)
    ll.append(30)
    ll.printList()
