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

        while curr is not None:
            print(curr.value, end=" ")
            curr = curr.next

    def findLoop(self, head):
        first = head  # self.head
        second = first.next.next  # self.head.next.next

        while first != second:
            first = first.next
            second = second.next.next
        first = head

        while first != second:
            first = first.next
            second = second.next
        return first
