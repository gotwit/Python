def getNodes():
    """Create linked list node value collection"""
    nodes = []
    n = int(input("Please enter the size of linked list: "))
    nodes[:n] = []
    # nodes[:n:-1] = []
    i = 1

    while i <= n:
        # print(f"Please enter {i} node value: ")
        x = int(input(f"Please enter {i} node value: "))
        nodes.append(x)
        # nodes[-1*i] = x
        i = i + 1
    # Reverse list or use nodes.insert(0, x) to insert at first position which shifts the nodes towards its right
    reversenodes = nodes[::-1]
    """ print(nodes)
    print(reversenodes) """
    return reversenodes
