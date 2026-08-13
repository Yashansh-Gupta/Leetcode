class Solution:
    def sumAndMultiply(self, n: int) -> int:
        l = []
        for i in str(n):
            if int(i) != 0:
                l.append(int(i))
        s = 0
        for i in l:
            s += i
        x = 0
        for i in l:
            x = x * 10 + i

        return x * s