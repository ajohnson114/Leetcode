class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      """
      You're caching the index and the buying state (i,bool). Base cases: i >= len(prices) -> return 0 and if (i,buying) in cache (set) return (i,buying)
      Recursive DFS. At every point you have the option to cool down which pretty much means to do nothing and to skip to the next day with the same 
      buying state (aka your willingness to buy or sell doesn't change after a buying day). On each day if you're willing to buy you want to calculate 
      how much profit you'll get if you buy that day which is the profit of the future days minus the expense of purchasing that day otherwise when you 
      compare this to choosing to cooldown on that day the maximum will be the result for that particular day. If you're not willing to buy that day
      you want to compare the options of selling which is the maximum profit generated from moving the index two days forward since you're forced to take 
      a cooldown day plus the money you get from selling today. Comparing that to choosing to do nothing that day i.e. coolingdown is your value for 
      dp[(i,buying)]. To finish your recursive dfs function you can return the cached value of the pairing you just calculated. Finally call the recursive
      dfs on your starting index and say you have a willingness to sell.
      """
        dp = {} # key is i and value is bool buy = True sell = False
        
        def dfs(i,buying):
            if i >= len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            
            cooldown = dfs(i+1, buying)
            if buying
                buy = dfs(i+1,not buying) - prices[i]
                dp[(i,buying)] = max(buy,cooldown)
            else:
                sell = dfs(i+2,not buying) + prices[i]
                dp[(i,buying)] = max(sell,cooldown)
            
            return dp[(i,buying)]
        
        
        return dfs(0,True)
                
            
