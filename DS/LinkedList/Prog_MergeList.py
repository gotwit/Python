class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def mergeLinkedLists(headOne, headTwo):
    h1 = headOne
    h2 = headTwo
    h1Prev = None

    while h1 is not None and h2 is not None:
        if h1.value < h2.value:
            h1Prev = h1
            h1 = h1.next
        else:
            if h1Prev is not None:
                h1Prev.next = h2
            h1Prev = h2
            h2 = h2.next
            h1Prev.next = h1
    if h1 is None:
        h1Prev.next = h2
    if headOne.value < headTwo.value:
        return headOne
    else:
        return headTwo
