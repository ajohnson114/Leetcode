def rob(self, nums: List[int]) -> int:
  """Basically rob1 is the 2 pointers away and rob2 is the house 1 pointer away. It's written this way since you can rob the first or second house in the
  beginning. For instance, [rob1, rob2, n, ... ,n+i]. At each step you will decide whether the maximal value at that point can be found by robbing
  the house before it or robbing the current house and the house 2 pointers away. The recurrence relation to remember is max(rob2, rob1 + n)
  
  """
        rob1, rob2 = 0,0
        
        for n in nums:
            temp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = temp
        
        return rob2
