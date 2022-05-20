class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Take the sum of the indices - the sum of the numbers given. You're not always
        going to be given the final number so you should add that in the beginning hence initializing it to len(nums)
        """
        res = len(nums)
        
        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res
