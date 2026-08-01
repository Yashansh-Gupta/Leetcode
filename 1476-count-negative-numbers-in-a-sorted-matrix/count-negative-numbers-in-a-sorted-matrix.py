class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])
        c=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]<0:
                    c+=1
        return c