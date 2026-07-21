class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q=set()
        for i in nums:
            q.add(i)

        nums[:]=q
        nums.sort()
        c=len(nums)
        return c