def swimInWater(self, grid: List[List[int]]) -> int:
  """
  Quick note you are guaranteed to reach the end! For this one, we need to do a BFS and traverse the grid. We will use a 
  minheap since we want to store the biggest path taken so far and the value by which we're sorting is the biggest height 
  (grid[i][j]) we've encountered in the path so far. When we reach the end we know that we've taken the ideal path since 
  we've always ordered it such that the lowest height path is the one taken first. 
  
  In our code we initialize the length of the grid since it is a square, a set to keep track of positions visited, 
  the minheap with the height, and position stored as a tuple and the directions in which we would need to traverse. 
  We then iterate while we still have values in the heap or until we return something. We first pop from the heap
  and then check to see if we're at the end, at which point we'll return the value. Then we'll do the check up, right,
  left, and down or if we've visited the position before then add the position to the visited set and push the value to 
  the heap. We're guaranteed to return something so we'll keep going until we do.
  """
        n=len(grid)
        visit = set()
        minheap = [[grid[0][0],0,0]]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        visit.add((0,0))

        while minheap:
            t,r,c = heapq.heappop(minheap)
            
            if r == n-1 and c==n-1:
                return t
            for dr,dc in directions:
                neiR, neiC = r+dr, c+dc
                if not (0 <= neiR < n) or not (0 <= neiC < n) \
                or (neiR,neiC) in visit:
                    continue
                visit.add((neiR,neiC))
                heapq.heappush(minheap,[max(t,grid[neiR][neiC]) , neiR,neiC])
