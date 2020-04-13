# A recursive funciton is said to be tail recursive if the recursive call is the last thing done by the function.
# There is no need to keep record of the previous state.


def fun(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
    fun(n - 1)


if __name__ == "__main__":
    fun(10)
