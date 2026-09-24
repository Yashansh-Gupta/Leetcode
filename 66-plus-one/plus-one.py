class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        q=''.join(map(str,digits))
        p=int(q)
        p+=1
        l=[]
        o=str(p)
        for i in range(len(o)):
            q=int(o[i])
            l.append(q)

        return l

        