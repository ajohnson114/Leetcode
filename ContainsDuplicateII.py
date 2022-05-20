class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      """
      We can check to see if the amount of unique elements is equal to the amount of elements and if we do then we can return False. Otherwise we can look
      at all the indices and if the absolute value of the subtracted indices is less than or equal to k and if the elements at those places are equal then
      we can return True. Otherwise return False
      """
        if len(set(nums)) == len(nums):
            return False
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(i-j) <= k:
                    if nums[i]==nums[j]:
                        return True
        return False
                
