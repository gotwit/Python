def cubesum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i * i * i
    return sum

# [(n * (n+1))//2]^2


def sumofcube(n):
    x = (n * (n + 1)) // 2
    return x * x


n = int(input("Enter a number: "))
# print(cubesum(n))
# print(sumofcube(n))
