start = 2
end = 50

count = 0
for val in range(start, end + 1):
    if val > 1:
        for i in range(2, val):
            if val % i == 0:
                break
        else:
            print(val, end=' ')
            print()


# Sieve of Eratosthenes Time complexity : O(n*log(log(n)))


def printPrime(n):
    prime = [True for i in range(n + 1)]
    # print(prime)
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            print(p, end=' ')
            print()


# if __name__ == '__main__':
    n = int(input("\nEnter a number to print all prime numbers: "))
    printPrime(n)


max_size = 1000001

isPrime = [True] * max_size
prime = []
spf = [None] * max_size  # Smallest Prime Factor

# O(N) time


def SieveOfEratosthenes(n):
    isPrime[0] = isPrime[1] = False

    for i in range(2, n):
        if isPrime[i] == True:
            prime.append(i)
            spf[i] = i

        j = 0

        while j < len(prime) and i * prime[j] < n and prime[j] <= spf[i]:
            isPrime[i * prime[j]] = False
            spf[i * prime[j]] = prime[j]
            j += 1


if __name__ == '__main__':
    n = 13
    SieveOfEratosthenes(n)

    i = 0
    while i < len(prime) and prime[i] <= n:
        print(prime[i], end=" ")
        i += 1
    print()
