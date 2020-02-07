# recursive
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

x = int(input("Enter a factorial number: "))
print("Factorial of {0} is {1}".format(x, factorial(x)))

# iterative
def ifactorial(n):
    x = 1
    if n <= 1:
        return 1
    while(n > 0):
        x = x * n
        n = n - 1
    return x

x = int(input("Enter a factorial number: "))
print(f"Factorial of {x} is {ifactorial(x)}")

