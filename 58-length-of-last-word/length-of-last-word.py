class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        q=[]
        c=0
        p=s.rstrip()
        q.append(p.split(" "))
        for i in q[0][-1]:
            c+=1
        return c