class Solution:
    def isPalindrome(self, x: int) -> bool:
        q=str(x)
        if q==q[::-1]:
            return True
        else:
            return False