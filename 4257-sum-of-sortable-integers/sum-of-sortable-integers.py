import math

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        drops = [0] * n
        for i in range(1, n):
            drops[i] = drops[i - 1] + (1 if nums[i] < nums[i - 1] else 0)
        def check_valid(k: int) -> bool:
            prev_max = -float('inf')
            for start in range(0, n, k):
                end = start + k
                internal_drops = drops[end - 1] - drops[start]
                circular_drop = 1 if nums[start] < nums[end - 1] else 0
                
                if internal_drops + circular_drop > 1:
                    return False
                block_min = min(nums[start:end])
                block_max = max(nums[start:end])
                
                if block_min < prev_max:
                    return False
                prev_max = block_max
            return True
        ans = 0
        for k in range(1, int(math.isqrt(n)) + 1):
            if n % k == 0:
                if check_valid(k):
                    ans += k
                if n // k != k:
                    if check_valid(n // k):
                        ans += n // k
                        
        return ans
