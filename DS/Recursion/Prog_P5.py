def fun(n):
    if n == 0:
        return
    fun(n // 2)
    print(n % 2, end=" ")


if __name__ == "__main__":
    fun(8)
