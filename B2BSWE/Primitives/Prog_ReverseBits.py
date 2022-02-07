class Solution:
    def reverseBits(self, x):
        output = 0

        while x != 0:
            output = output << 1

            if x & 1 == 1:
                output = output | 1
            
            x = x >> 1
        return output
        # Reverse bits

sln = Solution()
x = int(input("Enter a number: "))
rev = sln.reverseBits(x)
print(f"Reverse of {x} is {rev}")
