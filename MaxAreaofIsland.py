class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      """
      This is remeniscent of another problem although I'm not entirely sure which problem. Long story short, I first check to see if there is a grid and 
      if there isn't then we obviously won't find an island so we can return 0. Following that we set a variable to keep track of the biggest island we've
      found so far and then start defining our dfs. If the pointers in the matrix are out of bounds then we can return 0 similarly so if the grid is valued
      at a 0. A neat trick is that we can set the value in the grid to 0 to avoid using extra memory and then following this we can call dfs on all the 
      neighbors and add 1 to those results. Finally we run dfs on all the points in the grid and return the biggest value we find.
      """
        if not grid or not grid[0]:
            return 0
        
        biggest = 0
        
        def dfs(r,c):
            if (r < 0 or r >= len(grid)) or (c <0 or c>= len(grid[0])):
                return 0
            if grid[r][c]== 0:
                return 0
            
            grid[r][c]=0 #this marks the cell as visited and now we don't need 
            #extra memory
            
            return 1 + dfs(r-1,c) + dfs(r,c+1) + dfs(r+1,c) + dfs(r,c-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]==1:
                    biggest = max(biggest,dfs(r,c))
                    
        return biggest
