# from Utils.Prog_Utils import *
from Utils import Prog_Utils as util

def smallest(lst):
    return min(lst)

if __name__ == "__main__":
    # lst = getList()
    lst = util.getList()
    result = smallest(lst)
    print(f'Smallest of {lst} is {result}\n')