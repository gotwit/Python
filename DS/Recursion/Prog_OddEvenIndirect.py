# Indirect Recursion
# WAP to print numbers from 1 to 10 in such a way
# that when number is odd, add 1 and when number is even, substract 1.


def odd(n):
    if n <= 10:
        print(n + 1, end=" ")
        n += 1
        even(n)


def even(n):
    if n <= 10:
        print(n - 1, end=" ")
        n += 1
        odd(n)


if __name__ == "__main__":
    odd(1)
