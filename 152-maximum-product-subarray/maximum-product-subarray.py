class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxsum=0
        if len(nums)<2:
            return max(nums)
        if len(nums)==2:
            m=max(nums)
            q=nums[0]*nums[1]
            if q>m:
                return q
            else:
                return m
        for i in range(len(nums)):
            curr=nums[i]
            for j in range(i+1,len(nums)):
                curr*=nums[j]
                if maxsum<curr:
                    maxsum=curr
        if maxsum<max(nums):
            maxsum=max(nums)
        return maxsum
