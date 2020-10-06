""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]. """

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        indices = []

        n = len(nums)
        i = 0

        while (i+1) < n:
            if nums[i] + nums[i+1] == target:
                indices.append((i, i+1))
            i += 1
        return indices

lst = []
n = int(input("Enter the size of list: "))

for i in range(0, n):
    element = int(input(f"\nEnter {i} list element: "))
    lst.append(element)
target = int(input("\nEnter a target to find indexes: "))
sln = Solution()
result = sln.twoSum(lst, target)
print(f"{target} sum at indices {result}")