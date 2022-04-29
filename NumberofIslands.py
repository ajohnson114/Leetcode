class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      """
      First you want to check that we're not getting an empty array. Then we want to do a recursive dfs. We instantiate the amount of rows, the
      amount of columns, create a set to cache everything we've visited so far and an initial amount of islands. The we define the base case of our bfs
      to be if our row or columns is out of counds or if we've visited the place before or if it is 0 then we should return 0. After the base case, we
      can say that we've visited the place before, then we run dfs on all indices north south east and west of our current location. This should give you 
      all connected components. After doing this we can just iterate over all the rows and columns and if we reach something that is 1 and we haven't 
      explored then we should say that this is an island and we should run dfs on it. Finally we return our island count.
      """
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == "0" or
                (r, c) in visit):
                return 0
            
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands
