class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row=len(matrix)
        col=len(matrix[0])
        tr = [[0] * row for i in range(col)]

        for i in range(row):
            for j in range(col):
                tr[j][i]=matrix[i][j]
        return tr