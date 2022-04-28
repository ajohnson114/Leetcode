class Solution:
    def jump(self, nums: List[int]) -> int:
      """
      You want to do 1-D BFS in a sense. So you start at your first index and see what is the farthest into the list you can go from there. After you do
      this you will search the next part of your array which will start at the index to the right of your old right pointer and the new right pointer will
      be placed at the farthest place you could have reached previously. We do this until the right pointer has reached the last index and since we're 
      guaranteed to reach the last index we know that it always will so we increment our answer variable each time the loop runs until we reach the end.
      """
        ans = 0
        
        l,r = 0,0
        
        while r < len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i +nums[i])
            l = r+1
            r = farthest
            ans +=1
            
        return ans
            
        
