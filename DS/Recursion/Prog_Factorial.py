# Iterative
def ifact(n):
    res = 1

    while n > 0:
        res *= n
        n -= 1
    return res


# Recursive
def rfact(n):
    if n == 1:
        return 1
    else:
        return n * rfact(n-1)


if __name__ == "__main__":
    number = int(input("Please enter a number: "))
    print(f"Factorial of {number} by iterative method is {ifact(number)}\n")
    print(f"Factorial of {number} by recursive method is {rfact(number)}\n")
