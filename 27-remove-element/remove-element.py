class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        q=0
        for i in nums:
            if i==val:
                q+=1
        for i in range(q):
            nums.remove(val)
        c=len(nums)
        return c