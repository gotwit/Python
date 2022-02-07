class Solution:
    def isPowerOf2(self, x):
        # if x > 0:
        #     return (x & (x - 1)) == 0
        # else:
        #     return False

        return (x > 0 and (x & (x - 1)) == 0)

sln = Solution()
x = int(input("Enter a number: "))
res = sln.isPowerOf2(x)
print(x, "is power of 2" if res else "isn't power of 2")