import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        m = 10**9 + 7
        total = n + k - 1
        ans = 2 * k
        return math.comb(total, ans) % m
