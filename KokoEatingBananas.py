class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      """
      This isn't that bad once you see the trick. The trick is to run a binary search on the amount of bananas she can eat per hour and see which one allows
      her to eat all bananas if you sum the ceiling values of the banana piles divided by her rate. We know that the minimum she can eat is 1 banana/hour
      and the max that will matter is if she eats at a rate of the size of the biggest pile. So we initialize a left pointer to 1 and a right one to 
      max(piles) the size of the biggest pile. From there we binary search to find the smallest value that lets koko eat all bananas before the guards come 
      back. If we find a value k that does let her eat all bananas we want to check that that's the minimum so we set the right pointer to k-1 since we 
      want to check all values to the left of it otherwise we move the left pointer forward to k+1. 
      """
        l,r = 1, max(piles)
        res = r
        
        while l <=r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <=h : 
                res = min(res,k)
                r = k-1
            else:
                l = k+1
        
        return res
