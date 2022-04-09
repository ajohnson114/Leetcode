def maxProfit(self, prices: List[int]) -> int:
  """
  Basically you iterate backwards through the list and see the stock for the largest price you've seen so far. Update the largest profit as you go along
  backwards
  """
        maxprofit = 0
        biggest = prices[-1]
        for i in range(len(prices)-1,-1,-1):
            if prices[i] > biggest:
                biggest = prices[i]
            if biggest - prices[i] > maxprofit:
                maxprofit = biggest - prices[i]
        return maxprofit
