class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row=len(mat)
        col=len(mat[0])

        s=0
        for i in range(row):
            for j in range(col):
                if i==j:
                    s+=mat[i][j]
                elif i+j==col-1:
                    s+=mat[i][j]

        return s