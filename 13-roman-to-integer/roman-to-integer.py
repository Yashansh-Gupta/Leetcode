class Solution:
    def romanToInt(self, s: str) -> int:
        v = 0
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        r = 1
        for i in range(len(s)):
            if r >= len(s):
                v += d[s[i]]
            elif d[s[i]] < d[s[r]]:
                v -= d[s[i]]
            else:
                v += d[s[i]]
            r += 1
        return v