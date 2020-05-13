# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


def go(testCase):
    print(
        f"array: {testCase['array']}    maxSumIncreasingSubsequence: {maxSumIncreasingSubsequence(testCase['array'])}")


if __name__ == "__main__":
    # {"array":[], "method": }
    testCase1 = {"array": [10, 70, 20, 30, 50, 11, 30]}
    testCase2 = {"array": [1]}
    testCase3 = {"array": [-1]}
    testCase4 = {"array": [-1, 1]}
    testCase5 = {"array": [5, 4, 3, 2, 1]}
    testCase6 = {"array": [1, 2, 3, 4, 5]}
    testCase7 = {"array": [-5, -4, -3, -2, -1]}
    testCase8 = {"array": [8, 12, 2, 3, 15, 5, 7]}
    testCase9 = {"array": [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]}

    """ print("%(array)s %(method)s" %
          {testCase1["array"], maxSumIncreasingSubsequence(testCase1["array"])}) """
    go(testCase1)
    go(testCase2)
    go(testCase3)
    go(testCase4)
    go(testCase5)
    go(testCase6)
    go(testCase7)
    go(testCase8)
    go(testCase9)
