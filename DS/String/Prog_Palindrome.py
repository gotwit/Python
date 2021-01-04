class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

class Solution2:
    def isPlaindrome(self, s):
        for i in range(0, int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

class Solution3:
    def isPalindrome(self, s):
        return s == "".join(reversed(s))

class Solution4:
    def isPalindrome(self, s):
        r = ""

        for c in s:
            r = c + r
        return s == r

class Solution5:
    def isPalindrome(self, s):
        j = -1
        flag = 0

        for c in s:
            if c != s[j]:
                j = j-1
                flag = 1
                break
            j = j-1
        if flag:
            return False
        else:
            return True

n = int(input("Enter the number of test runs: "))
for i in range(0, n):
    result = ""
    s = str(input(f"Enter {i+1} string to check palindrome: "))
    # sln1 = Solution()
    # result = sln1.isPalindrome(s)

    # sln2 = Solution2()
    # result = sln2.isPlaindrome(s)

    # sln3 = Solution3()
    # result = sln3.isPalindrome(s)

    # sln4 = Solution4()
    # result = sln4.isPalindrome(s)

    # sln5 = Solution5()
    # result = sln5.isPalindrome(s)

    if result:
        print(f'{s} is palindrome')
    else:
        print(f"{s} isn't palindrome")