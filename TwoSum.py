class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      """
      Create a dictionary whose keys will be target - nums[i] and the value will be the index of nums[i] iterate through nums if the value you're looking 
      for is in nums it will be a key in the dictionary. Once you find the corresponding number return both indices.
      
      """
        dict_ = {}
        for i in range(len(nums)):
            if nums[i] in dict_:
                return [dict_[nums[i]],i]
            dict_[target-nums[i]] = i
