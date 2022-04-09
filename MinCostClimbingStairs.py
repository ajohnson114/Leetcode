def minCostClimbingStairs(self, cost: List[int]) -> int:
  """You initialize an empty array that you will fill with the cheapest costs to arrive at that index. From there we know that the cheapest costs to get to
  index 0 or 1 is cost[0] or cost[1] so we fill those in. From there we can see that we will jump from 1 or 2 squares behind and add the cost at our 
  current square to that value. The solution is min(arr[-1],arr[-2]) since we know that these are the two squares we can jump to the ending from
  """
        arr = [0] * len(cost)
        arr[0], arr[1] = cost[0], cost[1]
        
        for i in range(2,len(cost)):
            arr[i] = min(cost[i] + arr[i-1], cost[i] + arr[i-2])
            
        return min(arr[-1],arr[-2])
