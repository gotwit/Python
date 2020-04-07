import Prog_LRUCache as program
import unittest


letterMaps = {"a": 0, "b": 1, "c": 2, "d": 3,
              "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9}

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.checkLruOfSize(1)

    def test_case_2(self):
        self.checkLruOfSize(2)

    def test_case_3(self):
        self.checkLruOfSize(3)

    def test_case_4(self):
        self.checkLruOfSize(4)

    def test_case_5(self):
        self.checkLruOfSize(5)

    def test_case_6(self):
        self.checkLruOfSize(6)

    def test_case_7(self):
        self.checkLruOfSize(7)

    def test_case_8(self):
        self.checkLruOfSize(8)

    def test_case_9(self):
        self.checkLruOfSize(9)

    def test_case_10(self):
        self.checkLruOfSize(10)

    def checkLruOfSize(self, size):
        # Instantiate cache and insert first key.
        lru = program.LRUCache(size)
        self.assertEqual(lru.getValueFromKey("a"), None)
        lru.insertKeyValuePair("a", 99)
        self.assertEqual(lru.getMostRecentKey(), "a")
        self.assertEqual(lru.getValueFromKey("a"), 99)
        # Add existing key when cache isn't full.
        lru.insertKeyValuePair("a", 0)
        self.assertEqual(lru.getMostRecentKey(), "a")
        self.assertEqual(lru.getValueFromKey("a"), 0)
        # Add keys until cache reaches maximum capacity.
        for i in range(1, size):
            mostRecentLetter = letters[i - 1]
            self.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
            # Test key retrieval when cache isn't full.
            for j in range(0, i):
                letter = letters[j]
                self.assertEqual(lru.getValueFromKey(
                    letter), letterMaps[letter])
                self.assertEqual(lru.getMostRecentKey(), letter)
            currentLetter = letters[i]
            self.assertEqual(lru.getValueFromKey(currentLetter), None)
            lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
            self.assertEqual(lru.getMostRecentKey(), currentLetter)
            self.assertEqual(lru.getValueFromKey(
                currentLetter), letterMaps[currentLetter])
        # Add keys now that cache is at maximum capacity.
        for i in range(size, len(letters)):
            mostRecentLetter = letters[i - 1]
            self.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
            # Test key retrieval when cache is full.
            for j in range(i - size, i):
                letter = letters[j]
                self.assertEqual(lru.getValueFromKey(
                    letter), letterMaps[letter])
                self.assertEqual(lru.getMostRecentKey(), letter)
            leastRecentLetter = letters[i - size]
            currentLetter = letters[i]
            self.assertEqual(lru.getValueFromKey(currentLetter), None)
            lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
            self.assertEqual(lru.getMostRecentKey(), currentLetter)
            self.assertEqual(lru.getValueFromKey(
                currentLetter), letterMaps[currentLetter])
            self.assertEqual(lru.getValueFromKey(leastRecentLetter), None)
        # Add existing keys when cache is full.
        for i in range(len(letters) - size, len(letters)):
            currentLetter = letters[i]
            self.assertEqual(lru.getValueFromKey(
                currentLetter), letterMaps[currentLetter])
            lru.insertKeyValuePair(
                currentLetter, (letterMaps[currentLetter] + 1) * 100)
            self.assertEqual(lru.getValueFromKey(currentLetter),
                             (letterMaps[currentLetter] + 1) * 100)
