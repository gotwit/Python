# A recursive function is said to be non-tail recursive if the recursive call is not the last thing done by the function.
# After returning back, there is some statement or expression to evaluate.


def fun(n):
    if n == 0:
        return
    fun(n - 1)
    print(n, end=" ")


if __name__ == "__main__":
    fun(10)
