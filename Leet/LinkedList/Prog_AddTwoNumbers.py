class Node:
    def __init__(self, value = None):
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
            print(curr.value, end = " ")
            curr = curr.next
        print("\n")
    
    def printListAdvanced(self, head:Node):
        curr = head

        while curr:
            print(curr.value, end = " ")
            curr = curr.next
        print("\n")

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
        self.head = prev

class Solution:
    def addTwoNumbers(self, l1:Node, l2:Node):
        head = Node(0)
        curr = head
        carry = 0

        while l1 is not None or l2 is not None:
            x = l1.value if l1 is not None else 0 # Ternary condition
            y = l2.value if l2 is not None else 0 # Ternary condition
            totalSum = x + y + carry
            carry = totalSum//10
            digit = totalSum % 10 # Build a node for the sum of 1st list node value & 2nd list node value
            curr.next = Node(digit)
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            curr.next = Node(carry)
        return head.next

iterations = int(input("Enter the number of test runs: "))
k = 0
while k < iterations:
    # First Linked List
    m = int(input("Enter the size of 1st list: "))
    i = 0
    l1 = LinkedList()

    while i < m:
        x = int(input(f"Enter 1st list {i+1} node value: "))
        l1.push(x)
        i+=1
    print(f"Original Linked List 1")
    l1.printList()
    l1.reverse()
    print(f"Reverse Linked List 1")
    l1.printList()

    # Second Linked List
    n = int(input("Enter the size of 2nd list: "))
    l2 = LinkedList()
    i = 0

    while i < n:
        y = int(input(f"Enter 2nd list {i+1} node value: "))
        l2.push(y)
        i+=1
    print(f"Orignial Linked List 2")
    l2.printList()
    l2.reverse()
    print(f"Reverse Linked List 2")
    l2.printList()

    sln = Solution()
    result = sln.addTwoNumbers(l1.head, l2.head)
    lst = LinkedList()
    print(f"Sum of two linked list")
    lst.printListAdvanced(result)

    k = k + 1