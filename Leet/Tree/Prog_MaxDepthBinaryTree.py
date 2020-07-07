try:
    import os, sys

    sys.path.append(os.getcwd())
    
    from Utils import Prog_Utils as u
    import Prog_BinaryTree as bt
except Exception as e:
    print(f"Exception: {e}")

if __name__ == '__main__':
    lst = u.getIntList()
    n = len(lst)
    root = None

    binaryTree = bt.Tree()
    tree = binaryTree.build(lst, root, 0, n)
    depth = binaryTree.getHeightOrDepth(tree)
    
    print(depth)