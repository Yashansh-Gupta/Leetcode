class Solution:
    def mySqrt(self, x: int) -> int:
        q=1
        if x==0 or x==1:
            return x
        for i in range(x):
            if i*i>x:
                q=i-1
                break
        return q