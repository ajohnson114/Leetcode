def rob(self, nums: List[int]) -> int:
  """ The key to this solution is first noticing that the first and last values are not always the same so the array doesn't give you the circular 
  representation automatically. To overcome this we must run our HouseRobber algorithm on the array without the first element and another time 
  without the last element. Choosing the maximum of these two answers will lead us to the answer for HouseRobber2.
  
  House Robbers Solution:
  Basically rob1 is the 2 pointers away and rob2 is the house 1 pointer away. It's written this way since you can rob the first or second house in the
  beginning. For instance, [rob1, rob2, n, ... ,n+i]. At each step you will decide whether the maximal value at that point can be found by robbing
  the house before it or robbing the current house and the house 2 pointers away. The recurrence relation to remember is max(rob2, rob1 + n)
  """
        if len(nums) == 1:
            return nums[0]
        
        a,b = nums[0:len(nums)-1], nums[1:len(nums)]
        
        rob1, rob2 = 0,0
        
        for i in a:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        ans1 = rob2
        
        rob1, rob2 = 0,0
        
        for i in b:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        ans2 = rob2
        
        return max(ans1,ans2)  
