class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        r = 0

        for l in range(len(nums)):
            if l > r:
                return False

            if l + nums[l] > r:
                r = l + nums[l]

            if r >= len(nums) - 1:
                return True

        return False