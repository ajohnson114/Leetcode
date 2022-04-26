class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
      """
      You want to see what will happen if you add the current number to your current total and also what would happen if you subtracted it. The result
      is the total sum at your index. The base cases are if your index is out of bounds then you should return 1 if you found a combination that sums
      to your target otherwise return 0. Furthermore, we want to employ caching so if the (index, total) combination is in the cache we should return 
      the value associated with it. Once we calculate the values of dp[(i,total)] we should return the value and then call out function with the starting
      value. Note: we can also use lru_cache with max_size set to None for this solution
      """
        dp = {}
        
        def backtrack(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)] = backtrack(i+1,total+nums[i]) + backtrack(i+1, total-nums[i])
            
            return dp[(i,total)]
        
        return backtrack(0,0)
