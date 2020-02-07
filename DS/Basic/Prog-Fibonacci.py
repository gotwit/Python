def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        # for i in range(2, n):
        i = 2
        while i < n:
            print(f"a: {a}, b: {b}")
            c = a + b
            a = b
            b = c
            i += 1
        return b


# 0 1 1 2 3 5 8
# print(fib(9))


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 1 2 3 4 5 6 7 8 9
# 0 1 1 2 3 5 8 13 21
# print(fibonacci(9))

fibArr = [0, 1]


def fibonaci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(fibArr):
        return fibArr[n - 1]
    else:
        temp = fibonaci(n - 1) + fibonaci(n - 2)
        fibArr.append(temp)
        return temp


# print(fibonaci(9))
