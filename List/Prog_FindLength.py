from operator import length_hint


def findLength(lst):
    return length_hint(lst)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7]
    print('length of %(string)s is %(method)s' % {
        "string": str(lst),  "method": findLength(lst)})
