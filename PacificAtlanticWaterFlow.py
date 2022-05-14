class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        You want to go backwards from the oceans inwards and run dfs and see which ones you can make it to from both oceans. To do this we run dfs on the
        edges of the board and see what places we can make it to. Our dfs algorithm is parameterized by the position we're evaluating the sets we've 
        previously visited and the previous height we were at since we need to have a nondecreasing sequence. Our base case is if the position was visited 
        or if the position is out of bounds or if the height is decreasing in which cases we can just return. After the base case, we can add the position
        to the visited set and check all cardinal neighbors. Following that we can iterate on the columns and run dfs on the first and last rows and do 
        the same with the first and last columns. Finally we can check to see if the position is in both our pacific and atlantic sets and if so we can 
        add it to our output list.
        """
        
        rows, cols = len(heights), len(heights[0])
        
        pac,atl = set(), set()
        
        def dfs(r, c, visited, prevheight):
            if (r,c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevheight:
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
            
        
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        ans = []
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    ans.append([r,c])
        
        return ans
            
            
