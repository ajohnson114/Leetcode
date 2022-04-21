class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
      """
      This one isn't horrible. You want to iterate over all the coins and then for each coin you want to say that every index we will iterate over from the
      coin amount to the end is reachable by the value that it currently is plus i-coinamount since you can jump from (i-coinamount) to that index i. 
      From there all you need to do is return the index that is equal to amount.
      """
        dp = [0]*(amount+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
                
        return dp[-1]
