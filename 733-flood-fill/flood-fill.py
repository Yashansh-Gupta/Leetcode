class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        rows = len(image)
        cols = len(image[0])

        old = image[sr][sc]

        if old == color:
            return image #this checks if the image is already correct

        def fill(r,c):

            if image[r][c]==old:
                image[r][c]=color
            
                if r>0:
                    fill(r-1,c)
                if c>0:
                    fill(r,c-1)
                if r<rows-1:
                    fill(r+1,c)
                if c<cols-1:
                    fill(r,c+1)

        fill(sr,sc)
        return image


        


        