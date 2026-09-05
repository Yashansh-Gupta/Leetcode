from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=Counter(nums)
        l=[]
        for a,b in c.items():
            if b==1:
                l.append(a)
            elif b>=2:
                l.append(a)
                l.append(a)

        l.sort()
        for i in range(len(l)):
            nums[i] = l[i]
        return len(l)
