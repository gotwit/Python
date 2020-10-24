""" Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5. """

class Solution:
    def mergeArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        i = 0
        j = 0
        arr = []

        while i <= m and j <= n:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i = i + 1
            else:
                arr.append(nums2[j])
                j = j + 1
        return arr

m = int(input("\nEnter the size of first list: "))
n = int(input("\nEnter the size of second list: "))
nums1 = []
nums2 = []

for i in range(0, m):
    element = int(input(f"\nEnter first list {i} element: "))
    nums1.append(element)

for i in range(0, m):
    element = int(input(f"\nEnter second list {i} element: "))
    nums2.append(element)

sln = Solution()
result = sln.mergeArrays(nums1, nums2)
print(f"Merged array: {result}")