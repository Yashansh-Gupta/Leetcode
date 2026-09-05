class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        q = 1
        for i in range(len(nums)):
            ans[i] = q
            q *= nums[i]
        q = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= q
            q *= nums[i]
        return ans
        