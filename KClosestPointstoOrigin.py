class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      """
      Basically you instantiate a minheap and then have the minheap sort by the euclidean distances. From there pop k times and add each one to the answer
      list and return said list
      """
        def l2_dist(x,y):
            return math.sqrt(x**2 + y**2)
        
        temp = [(l2_dist(points[i][0], points[i][1]), points[i][0], points[i][1]) for i in range(len(points))]
        
        heapq.heapify(temp)
        
        ans = []
        
        while k >= 1:
            add = heapq.heappop(temp)
            ans.append([add[1],add[2]])
            k-=1
        
        return ans
