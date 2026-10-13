class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)
        n = len(nums)
        mid = n // 2
        subtracted_sum = sum(x * x for x in nums[:mid])
        added_sum = sum(x * x for x in nums[mid:])
        return added_sum - subtracted_sum
