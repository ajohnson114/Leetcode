class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """ When I talk about bigO I mean space time will always be at least O(m*n) since we have to visit all numbers
        This arises out of the O(m+n) solution which itself arises out of the O(n*m) solution. The O(n*m) solution is to make a copy of the matrix and 
        make changes in the matrix based on the original. The O(m+n) innovation is to see that we don't really need to use an entire matrix when we can 
        use two arrays: one the size of the amount of rows and one the size of the amount of columns. If we encounter a 0 in that row and column then we 
        mark it in the arrays corresponding places. Finally, from there the last innovation is to see that you can actually put these two arrays inside of 
        the matrix itself and do the operations in place. So you're putting it in the top row and the left column but your (0,0) square will have overlap
        so you will create a variable storing that piece of information. Thus we have set the stage for our solution. 
        
        We iterate through our entire matrix and if we find a 0 in any of the columns set the corresponding place in the first row equal to 0 and for rows
        we have two cases one where we're in the first row where we set our extra variable = to true and the other case where we set the row value in the 
        first column equal to 0. From there we fill in our 0's but the first row and column needs to be treated special becuase of our extra variable and
        the fact that they store information so we'll do those last. So we iterate from 1 to len rows and 1 to len columns and if the corresponding element
        in the 0th position in that row or column is 0 then we 0 out that element. Finally we check to see if the top column should be 0'd out and that bit 
        of information is stored in (0,0) so if that's 0 we set our first column equal to 0 by iterating over the rows. Finally, we should check if the first
        row should be 0 by checking our extra variable and if it is 0 out that row by iterating over the columns and that's it
        """
        
        rows, columns = len(matrix), len(matrix[0])
        row0 = False
        
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row0 = True
                
        
        for r in range(1,rows):
            for c in range(1,columns):
                if matrix[0][c]==0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if row0:
            for c in range(columns):
                matrix[0][c] = 0
