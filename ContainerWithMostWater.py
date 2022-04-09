def maxArea(self, height: List[int]) -> int:
"""
The key to this is to realize you want to maximize the heights of l and r at each time step. You start with a 2 pointer approach and initialize your 
answer to 0. From there you calculate the current area and then compare it to your result (for the first step this seems silly but the comparison is 
useful later). If the current area is bigger that is your max area. Since you have your current area you now have to iterate the loop and you would like
to do so in a way that you hopefully get the 2 biggest heights so you iterate the pointer with the smaller height. The while loop is initialized with 
l<r because area would be 0 if l==r.
""" 
  
    l,r = 0,len(height)-1
    res = 0
    while l<r:
        area = (r-l)*min(height[l],height[r])
        res = max(area,res)
        if height[l] < height[r] :
            l+=1
        else:
            r-=1

    return res
