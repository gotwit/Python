# A subsequence of an array is a set of numbers that aren't
# necessarily adjacent in the array but that are in the
# same order as they appear in the array. For instance, 
# the numbers [1, 3, 4] form a a subsequcne of the array
# [1, 2, 3, 4], and so do the numbers [2, 4].
# Note that a single number in an array and the array itself
# are both valid subsequence of the array.

import unittest

class program:
    def isValidSubsequence(self, array, sequence):
        arrIdx = 0
        seqIdx = 0

        while arrIdx < len(array) and seqIdx < len(sequence):
            if array[arrIdx] == sequence[seqIdx]:
                seqIdx += 1
            arrIdx += 1
        return seqIdx == len(sequence)
    
    def isValidSubsequenceV2(self, array, sequence):
        seqIdx = 0

        for value in array:
            if seqIdx == len(sequence):
                break
            if value == sequence[seqIdx]:
                seqIdx += 1
        return seqIdx == len(sequence)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(program().isValidSubsequenceV2(array, sequence))

    def test_case_2(self, test_cases):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 100]
        # self.assertTrue(program().isValidSubsequenceV2(array, sequence) == True)
        # self.assertTrue(program().isValidSubsequenceV2(array, sequence))

        with self.assertRaises(AssertionError) as contextManager:
            # print(f"Assertion Error not raised")
            self.assertTrue(program().isValidSubsequenceV2(array, sequence))
        print(f"Exception: Invalid Subsequence, {contextManager.exception}")
        
    def run_tests(self, test_cases):

        for key, value in enumerate(test_cases):
            array, sequence = value["array"], value["sequence"]
            result = "Valid sequence" if program().isValidSubsequence(array, sequence) else "Invalid sequence"
            print(f"test_cases_{key + 1} Array: {array}, Sequence: {sequence} {result}\n")
        

if __name__ == "__main__":
    TestProgram().test_case_1()
    TestProgram().test_case_2([])


    test_cases = [{"array": [5,1,22,25,6,-1,8,10],"sequence": [1,6,-1,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,1,22,25,6,-1,8,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,1,22,6,-1,8,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [22,25,6]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [1,6,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,1,22,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,-1,8,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [25]},
    {"array": [1,1,1,1,1],"sequence": [1,1,1]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,1,22,25,6,-1,8,10,12]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [4,5,1,22,25,6,-1,8,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,1,22,23,6,-1,8,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,1,22,22,25,6,-1,8,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,1,22,22,6,-1,8,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [1,6,-1,-1]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [1,6,-1,-1,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [1,6,-1,-2]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [26]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,1,25,22,6,-1,8,10]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,26,22,8]},
    {"array": [1,1,6,1],"sequence": [1,1,1,6]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [1,6,-1,10,11,11,11,11]},
    {"array": [5,1,22,25,6,-1,8,10],"sequence": [5,1,22,25,6,-1,8,10,10]}]


TestProgram().run_tests(test_cases)