class Solution:
    def search(self, nums: List[int], target: int) -> int:
      """
      This is something you need to sort of visualize. You have to imagine a diagonal arrow that has been cut in two and the beginning part has been 
      concatenated onto the end (the arrow ends and the beginning portion is right there.) So at each part of the search we need to decide what part of that
      arrow we're on. 
      
      If the number we're currently looking at is bigger than or equal to our left pointer we should at how our target is compared to where
      our pointers are. If the target is greater than our current middle we know we need to move the left pointer up like normal binary search but if 
      our left pointer is <= our middle pointer and the target is smaller than our left pointer, we know that we were on the part of the arrow with the ending
      rather than that of the beginning and we need to change to that other part of the arrow that contains the beginning. 
      
      Otherwise if the target is less than our middle pointer value we move the right pointer like normal binary search but if target is bigger than our 
      right pointer value then we know we need to search the left part of the list (the part of the arrow that has the ending). If the value at mid is 
      our target then we're good to go otherwise return -1.
      """
        l,r = 0, len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            #check what part of array we're in
            
            #left portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid +1
                else:
                    r = mid -1
            #right portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid +1
            
        return -1
