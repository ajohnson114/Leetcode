class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      """
      We can just see if the amount of unique elements doesn't matches the amount of elements in the array. If it does then we return False (since it 
      doesn't contain a duplicate) otherwise we return True. We can also iterate through a use a dictionary
      """
        """dict_ = {}
        for i in nums:
            if i in dict_:
                return True
            dict_[i]=0
        return False"""
        
        return len(set(nums)) != len(nums)
        
