def sumofsquares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


def squaresum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i * i
    return sum


# n = int(input("Enter a number: "))
# print(sumofsquares(n))
# print(squaresum(n))
