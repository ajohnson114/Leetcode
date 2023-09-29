def orangesRotting(self, grid: List[List[int]]) -> int:
  """
  This is a BFS problem honestly raeding the question here makes a really big difference as prior to seeing the neetcode solution I 
  didn't know that there could be more than 1 rotten orange in the grid to start 
  Basically, what you wanna do to solve the problem is that you want to add the positions of all the rotten oranges to the queue at the 
  start and also count the amount of fresh oranges, as that will help us in the stopping condition for the BFS. In our BFS we iterate
  for the amount of rotten oranges we collected at the last level and check the cells around it, if it is in bound and a fresh orange we 
  make it rotten, add it to the q and decrement the fresh orange counter. After we iterate through the entire level we can increment the 
  time count. The while loop will end when all the fresh oranges are converted to rotten oranges or when there are no more possible 
  cells to turn rotten anymore i.e. the q is empty. We can then return the time if fresh==0 since that's what the question is asking 
  and if it is not equal to 0 we can just return -1
  """
        q = deque()
        fresh,time = 0,0

        m,n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh += 1 

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while q and fresh > 0:
            qlen = len(q)
            for i in range(qlen):
                r, c = q.popleft()
                for x,y in dirs:
                    row,col = x+r,y+c
                    if not (0<=row<m and 0<=col<n) or grid[row][col]!=1:
                        continue
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh-=1
            time +=1
        return time if fresh == 0 else -1
                    

