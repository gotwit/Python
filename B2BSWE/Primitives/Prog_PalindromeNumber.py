import math

class Solution:
    def isPalindrome(self, x):
        # rtype: bool
        if(x < 0):
            print("Enter a +ve number")
            return False
        logx = math.log10(x)
        digits = int(math.floor(logx))
        totalDigits = digits + 1
        mask = 10**digits #int(math.pow(10, digits)) # or use x**y
        length = int(totalDigits/2)

        for i in range(totalDigits//2):
            leftDigit = int(x / mask)
            rightDigit = int(x % 10)

            if leftDigit != rightDigit:
                return False
            
            x = int(x % mask)
            x = int(x / 10)
            mask = mask // 100

        # print(digits)

        return True
        None

sln = Solution()
x = int(input("Enter a number: "))
if(sln.isPalindrome(x)):
    print(f"{x} is palindrome")
else:
    print(f"{x} isn't palindrome")