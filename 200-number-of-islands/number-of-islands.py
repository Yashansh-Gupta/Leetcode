class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(r,c):
            if grid[r][c]=="1":
                grid[r][c]="0"
                if r>0:
                    dfs(r-1,c)
                if c>0:
                    dfs(r,c-1)
                if r<row-1:
                    dfs(r+1,c)
                if c<col-1:
                    dfs(r,c+1)

        row=len(grid)
        col=len(grid[0])
        islands=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    islands+=1
                    dfs(i,j)
        return islands

