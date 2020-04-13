# Non-tail recursive


def fun(n):
    if n == 1:
        return 0
    else:
        # Non-tail recursive, since there is an expression to evaluate after return from fun(n/2) call.
        return 1 + fun(n // 2)


if __name__ == "__main__":
    fun(8)
