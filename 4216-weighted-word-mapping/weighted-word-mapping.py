class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        l=[]
        for i in range(len(words)):
            x=0
            for j in range(len(words[i])):
                q=ord(words[i][j])-97
                p=weights[q]
                x+=p

            x=x%26
            l.append(chr(ord('z')-x))
        return ''.join(l)
        
