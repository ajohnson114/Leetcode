class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      """
      This is interesting. So you want the maximum of a sliding window. The trick here is to realize that if you have a sorted list of numbers you could
      just look at one of the ends and see that that's the biggest number in O(1) time. A deque is a data structure that lets you access both ends of the 
      data structure in constant time. You are storing this in decreasing order so the biggest value will always be on the left. Here we store indices 
      but you can also solve this with values. We start a 2 pointer approach and we say that while the value of the biggest element in the deque is smaller
      than our current value we remove it since we will never need it since we only care about the maximum. Then we add the new element which will be the
      biggest so far. We then need to check our pointers to see our pointers are still in bound since we're storing pointers the left pointer being bigger
      than the first element means that the leftmost element in the deque is no longer in our window so we can pop it. Furthermore, if the right pointer is 
      bigger than our window we know that we should start adding to our solution output variable. So we add the left most element which is the biggest we've
      seen so far and then iterate our left pointer to keep our window tight. After that step we can iterate our right pointer and continue the cycle.
      
      
      """
        sol = []
        l = r = 0
        dq = collections.deque()
        
        while r < len(nums):
            #pop smaller values from dq
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
                
            dq.append(r)
            
            #remove left value from window
            if l > dq[0]:
                dq.popleft()
            
            if (r+1) >= k:
                sol.append(nums[dq[0]])
                l+=1
            
            r +=1
                
            
        
        return sol
