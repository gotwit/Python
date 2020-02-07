import math


def isPerfectSquare(n):
    x = int(math.sqrt(n))
    return x * x == n


def isFibonacci(n):
    return isPerfectSquare(5 * (n * n) + 4) or isPerfectSquare(5 * (n * n) - 4)


n = int(input("Enter a number to check if it is fibonacci: "))

for i in range(1, n + 1):
    if isFibonacci(i):
        print(f"{i} is fibonacci")
    else:
        print(f"{i} is not fiboacci")
