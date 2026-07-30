class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row=len(mat)


        s=0
        for i in range(row):
            s+=mat[i][i]
            j = row - 1 - i
            if i!=j:
                s+=mat[i][j]
        return s
