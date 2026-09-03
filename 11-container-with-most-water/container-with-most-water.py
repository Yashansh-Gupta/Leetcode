class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        if left==right:
            return 0
        m=0
        while left<right:
            w=min(height[left],height[right])
            r=abs(left-right)
            c=w*r
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

            if c>m:
                m=c
            

        return m
