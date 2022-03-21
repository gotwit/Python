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
        # mask = 10**(totalDigits - 1) #int(math.pow(10, digits)) # or use x**y

        length = int(totalDigits/2)

        for i in range(totalDigits//2):
            leftDigit = int(x / mask)
            rightDigit = int(x % 10)

            if leftDigit != rightDigit:
                return False
            
            x = int(x % mask)
            x = int(x / 10)
            # Simple divide mask by 10^no of digits removed
            mask = mask // 100

            # Below code block could be used to find mask with added time complexity.
            """ if x > 0:
                logx = math.log10(x)
                digits = int(math.floor(logx))
                # totalDigits = digits + 1
                mask = int(math.pow(10, digits)) """

        # print(digits)

        return True
        None

sln = Solution()
x = int(input("Enter a number: "))
if(sln.isPalindrome(x)):
    print(f"{x} is palindrome")
else:
    print(f"{x} isn't palindrome")