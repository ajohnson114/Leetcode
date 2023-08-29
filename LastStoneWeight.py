class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      """This is a heap question and heaps in python are implemented as minheaps. So to start I make everything negative. Then I start a loop while the length of the heap is 
      greater than 1. While that is we just follow the instructions given, delete (which I program here as just doing nothing) if they are equal and append the difference if 
      they are different. I put in the naegative of the difference because all the things in the heap are negative but I take the difference in the positives. Finally, I 
      return the last thing in the array if there is something there if there is something else return 0"""
        h = [-i for i in stones]
        heapq.heapify(h)

        while len(h) > 1:
            y = abs(heapq.heappop(h))
            x = abs(heapq.heappop(h)) if h else 0

            if x != y:
                y = y-x
                heapq.heappush(h, -y)

        
        return abs(h[0]) if h else 0
