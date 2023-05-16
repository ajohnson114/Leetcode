def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
  """
  This is kinda a standard DFS problem but you need to make some slight changes. First we initialize our dp matrix so we 
  can memoize solutions, and we have the dimensions (to make things easier) and the ways we want to traverse. As a quick 
  note we set the dp matrix to 0 so we can check to see if we have visited the position before. In our dfs function,
  if we haven't visited the before we initialize a variable to hold our max element then check the directions we want to 
  traverse. As long as the position is in our matrix and the value at the position is greater than our current value we 
  say that our value at this position is the bigger of the max variable or the dfs function evaluated at the new position
  +1. We then return the value at our current position. Next we call the function on each position in our matrix and get the
  biggest element in our dp matix (plus 1 since we initialized all our positions to 0 but technically each position has a 
  path with itself).
  
  """
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix), len(matrix[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        dp = [[0]*n for _ in range(m)]

        def dfs(x,y):
            if not dp[x][y]:
                biggest = 0
                for i,j in directions:
                    if not 0<=x+i<m or not 0<=y+j<n :
                        continue
                    if matrix[x+i][y+j] > matrix[x][y]:
                        biggest = max(dfs(x+i,y+j)+1, biggest)
                dp[x][y] = biggest
            
            return dp[x][y]
        
        for i in range(m):
            for j in range(n):
                dfs(i,j)

        return max([max(row) for row in dp])+1
