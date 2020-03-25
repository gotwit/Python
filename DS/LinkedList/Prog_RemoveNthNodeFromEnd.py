class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next

    def removeNthNodeFromEnd(self, head, k):
        curr = head
        len = 0

        while curr:
            len += 1
            curr = curr.next

        i = 0
        prev = None
        curr = head
        while i < len - k:  # and curr.next is not None:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = curr.next

# using 2 pointer
# def removeKthNodeFromEnd(self, head, k):


def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    counter = 1
    # <= inclusive of the kth node for second pointer is ahead of first pointer
    while counter <= k:
        counter += 1
        second = second.next

    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next


if __name__ == '__main__':
    """Main method"""
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
    print(nodes)
    print(reversenodes)

    ll = LinkedList()

    for node in reversenodes:
        ll.push(node)

    ll.printList()

    k = int(input("Please enter kth node to remove from end\n"))
    ll.removeNthNodeFromEnd(ll.head, k)

    ll.printList()


"""     lnklist = LinkedList()
    lnklist.push(5)
    lnklist.push(4)
    lnklist.push(3)
    lnklist.push(2)
    lnklist.push(1)

    print("Linked List")
    lnklist.printList() """
