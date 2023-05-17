def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
  """
  This is Bellman-Ford. The point of this is we start out a prices array to be infinity and we want to see if we can reach
  them in for the minimum prices. The way the algorithm works is that it costs nothing to arrive where you start from so 
  we set that equal to 0 then we loop k+1 times, create a copy of the prices array as we want to update that and then
  check to see if the price to reach a destimate is less than the price to reach the source + the price to reach the
  destination. If it is then we update the price of the destination to the price it took to reach the source + the 
  price to reach the destination. At the end of each loop we update our global prices array and return the cost to reach
  our destination if it's not infinity.
  """
        prices = [float('inf')]*n
        prices[src] = 0

        for i in range(k+1):
            tempprices = prices.copy()
            for s,d,p in flights: #s: source d:dest p:price
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tempprices[d]:
                    tempprices[d] = prices[s] + p

            prices = tempprices
        
        return prices[dst] if prices[dst] != float('inf') else -1
