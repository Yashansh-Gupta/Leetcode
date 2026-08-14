class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=[]
        q=[]
        c=0
        for i in range(len(s)):

            if s[i] not in l:
                l.append(s[i])
            elif l.count(s[i])<2:
                l.append(s[i])

            else:
                c=len(l)
                q.append(c)
                while l.count(s[i])>=2:
                    l.remove(l[0])
                l.append(s[i])
        q.append(len(l))
        return max(q)