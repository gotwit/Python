def get(n):
    if n < 1:
        return
    get(n - 1)
    get(n - 3)
    print(n, end=" ")


if __name__ == "__main__":
    callCount = 1
    get(6)
