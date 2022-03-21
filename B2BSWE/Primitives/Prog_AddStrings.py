class Solution:
    def addString(self, s1, s2):
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += ord(s1[i]) - ord('0')
                i -= 1
            
            if j >= 0:
                sum += ord(s2[j]) - ord('0')
                j -= 1
            
            carry = int(sum / 10)
            result += str(sum % 10)

        if carry != 0:
            result += str(carry)
        
        rev = result[::-1]
        return rev

        None

sln = Solution()
str1 = input("Enter 1st number: ")
str2 = input("Enter 2nd number: ")
res = sln.addString(str1, str2)
print("Sum of ", str1, " and ", str2, " is", res)