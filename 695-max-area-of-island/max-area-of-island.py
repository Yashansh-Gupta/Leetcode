class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])

        def dfs(r, c):

            if r < 0 or r >= row or c < 0 or c >= col:
                return 0

            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return (
                1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1)
                + dfs(r, c + 1))

        maxs=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    if area>maxs:
                        maxs=area
        return maxs

