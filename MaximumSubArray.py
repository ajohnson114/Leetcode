def maxSubArray(self, nums: List[int]) -> int:
  """
  So long as the previous indexes value will add something to the current sum we'll take it otherwise we skip it. Each index will have the maximum
  subarray that ends at that index and we just return the biggest one.
  """
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
