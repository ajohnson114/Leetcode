#Solution1

def trap(self, height: List[int]) -> int:
  """
  The key to understanding this solution is to see that you want the minimum of the biggest of the heights on either side of your index as that will 
  tell you the biggest wall you can use to trap rain water with. So you iterate through 2 times trying to find the biggest wall to the left of your index
  and to right of your index. Then you take the minimum of those 2 to say this is the biggest amount of rain water we can theoretically trap. Finally,
  We have to take the height of the block at our index into account. You know you can't trap less water than 0 so if the difference between the biggest
  wall and the height at your index is positive or 0 you should set the amount of rainwater trapped at that index. Finally, the answer is the sum of that.
  """
        maxl = [0] *len(height)
        maxr = [0] *len(height)
        
        big = 0
        for i in range(len(height)):
            if height[i] > big:
                big = height[i]
            maxl[i] = big
        
        big = 0
        for i in range(len(height)-1,-1,-1):
            if height[i] > big:
                big = height[i]
            maxr[i] = big
        
        minlr = [min(maxl[i],maxr[i]) for i in range(len(height))]
        
        ans = [minlr[i] - height[i] if minlr[i] - height[i] > 0 else 0 for i in range(len(height))]
        
        return sum(ans)
      
#Solution 2
 def trap(self, height: List[int]) -> int:
    """
    To solve this with a 2 pointer approach you basically create your two pointers and separate variables to see the biggest numbers each pointer has 
    seen so far. We know that we'll take the minimum from the maxleft and maxright pointer and we're almost guaranteed to have a bigger element on the 
    other side since we know that they're going to be a max right. From this we can do the same minl(r) - height[i] addition we did last time. 
    """
        if not height:
            return 0
        
        l,r = 0,len(height)-1
        maxl, maxr = height[l], height[r]
        res = 0
        
        while l < r:
            if maxl < maxr:
                l +=1
                maxl = max(maxl,height[l])
                res += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr,height[r])
                res += maxr - height[r]
            
        return res
