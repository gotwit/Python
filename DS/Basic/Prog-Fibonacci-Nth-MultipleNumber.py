# Solution 1
def findPosition(k, n):
    """ n’th multiple of a number in Fibonacci Series """
    f1 = 0
    f2 = 1
    i = 2
    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k == 0:
            return n * i
        i += 1

# Solution 2


def findFibPos(k, n):
    arr = [0, 1]

    f1 = arr[0]
    f2 = arr[1]
    i, count = 2, 0

    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        arr.append(f2)

        if arr[i] % k == 0:
            count += 1

        if count == n:
            return i
        """ if i == 11:
            break """
        i += 1
    # return arr
    return 0


""" 
n = 1000  # 5
k = 10  # 4 """

n = 5
k = 4

print("Position of n'th multiple of k in "
      "Fibonacci Seires is", findPosition(k, n))

print("Position of n'th multiple of k in "
      "Fibonacci Seires is", findFibPos(k, n))
