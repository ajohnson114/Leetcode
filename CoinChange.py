def coinChange(self, coins: List[int], amount: int) -> int:
  """What you want to do is initialize a list of values from 1 to amount size and figure out the least amount of coins necessary to make that amount with
  the coins in your position. Since you want to reduce the amount of coins you have and you know that you will never have more than amount coins (the case
  where the easiest way to give you the amount is in pennies) amount +1 is a safe variable to initialize the list to. From there you iterate over all the 
  values from 0 to amount trying to see if you can subtract the value of 1 coin to use the value of a subproblem you already solved before.
  If you can use the value of a subproblem you solved before then you choose between the minimum of that solved subproblem + the coin you just added
  and the value that was already there. The final answer should be at index: amount since that is the subproblem that tells you the way to make the 
  amount with the least amount of coins
  """
        ans = [amount+1]*(amount+1)
        ans[0] = 0
        
        for i in range(1,amount+1):
            for c in coins:
                if i-c >= 0:
                    ans[i] = min(ans[i],ans[i-c]+1)
        
        return ans[amount] if ans[amount] != amount+1 else -1
