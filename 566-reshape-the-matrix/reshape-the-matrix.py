class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """


        tr=[[0]*c for i in range(r)]

        row=len(mat)
        col=len(mat[0])
        l=[]
        if row * col != r * c:
            return mat

        for i in range(row):
            for j in range(col):
                l.append(mat[i][j])

        k=0
        for i in range(r):
            for j in range(c):
                if k<len(l):
                    tr[i][j]=l[k]
                    k+=1
        return tr