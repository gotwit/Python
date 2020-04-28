# O(nd) time | O(1) space
def minNoOfCoinsForChange(n, denoms):
    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0

    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(
                    numOfCoins[amount], 1 + numOfCoins[amount - denom])

    return numOfCoins[n] if numOfCoins[n] != float("inf") else - 1


if __name__ == "__main__":
    denoms = [1, 5, 10]
    n = len(denoms)
    print(f"Min coins {minNoOfCoinsForChange(n, denoms)}")
