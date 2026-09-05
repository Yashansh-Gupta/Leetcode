class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            if citations[0] > 0:
                return 1
            else:
                return 0

        ans = 0

        for i in range(len(citations)):
            c = 0
            h = i + 1

            for j in citations:
                if j >= h:
                    c += 1

            if c >= h:
                ans = h

        return ans