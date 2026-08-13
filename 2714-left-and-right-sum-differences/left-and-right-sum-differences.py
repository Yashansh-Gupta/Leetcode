class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[]
        leftsum=[0]
        for i in range(0,len(nums)-1):
            leftsum.append(nums[i]+leftsum[-1])
        
        rightsum=[0]
        for i in range(-1,-len(nums),-1):
            rightsum.append(nums[i]+rightsum[-1])
        rightsum.reverse()

        for i in range(len(leftsum)):
            q=leftsum[i]-rightsum[i]
            if q<0:
                q=-q
            l.append(q)
        return l





