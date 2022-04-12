class Solution:
    def findMin(self, nums: List[int]) -> int:
      """
      This is binary search with a twist. Similarly to search rotated sorted array we have two sorted portions of the list. So we need to decide which part
      of the list we're in. As a quick note, this algorithm only works within the context of this rotated array and doesn't work in the case of a normal
      sorted array so we must include a if statement that checks for that and returns the element all the way to the left in that case. Otherwise
      we calculate the middle and see if it is smaller than our current smallest. We then compare our mid pointer to our left pointer and if the mid 
      value is bigger or equal to our left value we should search the right side of our list (because we already checked to see if that part of the array 
      was sorted and would have returned the smallest in that case we don't need to worry about the answer being there). Otherwise we need to search the 
      left side of our list. Following all this we will know that we searched our entire array and just need to return the smallest element found so far now.
      """
        l,r = 0,len(nums)-1
        smallest = nums[0]
        
        while l<=r:
            if nums[l] < nums[r]:
                smallest = min(smallest,nums[l])
                break
            
            mid = (l+r) //2
            smallest = min(smallest,nums[mid])
                
            if nums[mid] >= nums[l]:
                l = mid +1
                
            else:
                r = mid - 1 
                
        return smallest
