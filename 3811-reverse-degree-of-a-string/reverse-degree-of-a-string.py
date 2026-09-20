class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0  
        for i, c in enumerate(s, 1):
            reverse = 26 - (ord(c) - ord('a'))
            ans += reverse * i  
        return ans
