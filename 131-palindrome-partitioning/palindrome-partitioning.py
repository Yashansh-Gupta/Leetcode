class Solution:
    def partition(self, s):
        ans = []
        path = []

        def backtrack(start):
            if start == len(s):
                ans.append(path.copy())
                return

            for r in range(start, len(s)):
                part = s[start:r+1]

                if part == part[::-1]:
                    path.append(part)

                    backtrack(r + 1)

                    path.pop()

        backtrack(0)
        return ans