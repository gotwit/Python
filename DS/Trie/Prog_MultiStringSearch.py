# Solution 1
# O(bns) time | O(n) space
# b - length of big string, n - number of small strings, s - length of biggest or largest small string in small strings list


""" def multiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]


def isInBigString(bigString, smallString):
    for i in range(len(bigString)):
        if i + len(smallString) > len(bigString):
            break
        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False


def isInBigStringHelper(bigString, smallString, startIdx):
    leftBigIdx = startIdx
    rightBigIdx = startIdx + len(smallString) - 1
    leftSmallIdx = 0
    rightSmallIdx = len(smallString) - 1

    while leftBigIdx <= rightBigIdx:
        if bigString[leftBigIdx] != smallString[leftSmallIdx] or bigString[rightBigIdx] != smallString[rightBigIdx]:
            return False
        leftBigIdx += 1
        rightBigIdx -= 1
        leftSmallIdx += 1
        rightSmallIdx -= 1
    return True """

# Solution 2
# O(b^2 + ns) time | O(b^2 + n) space
# b^2 for creating SuffixTrie, n - number of small strings, s - length of largest small string

""" 
def multiStringSearch(bigString, smallStrings):
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)

    return [modifiedSuffixTrie.contains(string) for string in smallStrings]


class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    def contains(self, string):
        node = self.root

        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True
 """

# Solution 3
# O(ns + bs) time | O(ns) space


def multiStringSearch(bigString, smallStrings):
    trie = Trie()

    for string in smallStrings:
        trie.insert(string)
    containedStrings = {}

    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, trie, containedStrings)


def findSmallStringsIn(string, startIdx, trie, containedStrings):
    currentNode = trie.root

    for i in range(startIdx, len(string)):
        currentChar = string[i]
        if currentChar not in currentNode:
            break
        currentNode = currentNode[currentChar]
        if trie.endSymbol in currentNode:
            containedStrings[currentNode[trie.endSymbol]] = True


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def insert(self, string):
        node = self.root
        for i in range(len(string)):
            if string[i] not in node:
                node[string[i]] = {}
            node = node[string[i]]
        node[self.endSymbol] = string


if __name__ == "__main__":
    bigString = "this is a big string"
    smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
    print(multiStringSearch(bigString, smallStrings))
