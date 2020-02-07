def isPrime():
    num = None
    try:
        num = int(input("Enter a number to check if it is prime or not: "))

        if num > 1:
            for i in range(2, num // 2):
                if not num % i:
                    print(num, " is not a prime number")
                    break
            else:
                print("{0} is a prime number".format(num))
        else:
            print(f"{num} is not a prime number")

    except Exception:
        print(f"Error: {num} not a valid number")

# no overloading


def checkPrime(n) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


print(checkPrime(11))

print(checkPrime(311))

print(checkPrime(251))

print(checkPrime(74))
