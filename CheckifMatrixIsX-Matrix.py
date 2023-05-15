def checkXMatrix(self, grid: List[List[int]]) -> bool:
  """
  I feel that the comments do this problem justice
  """
        n = len(grid)
        visited = set()

        for i in range(n):
            # Check to see if the left to right diagonal is non-zero
            if grid[i][i] != 0:
                visited.add((i,i)) # add it so we know it's a diagonal ele
            else:
                return False

            # Check to see if the right to left diagonal is non-zero
            if grid[0+i][n-1-i] != 0: #this indexing is tricky
                visited.add((0+i,n-i-1)) 
                # start in first row at rightmost col
                # and add it so we know it's a diagonal ele
            else:
                return False

        for i in range(n):
            for j in range(n):
                if (i,j) in visited: #if it's a diagonal element skip
                    continue
                elif grid[i][j]!= 0: #if it's not diag ele and non zero
                    return False #we return False

        return True #after all checks if we reach here it passes
