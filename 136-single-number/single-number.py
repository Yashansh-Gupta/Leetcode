class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q=set()
        for i in range(len(nums)):
            if nums[i] not in q:
                q.add(nums[i])
            else:
                q.remove(nums[i])
        return q.pop()

