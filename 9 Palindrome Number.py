# Method 1 Python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string1 = str(x)
        string2 = string1[::-1]
        if string1 == string2 :
            return True
        return False
