def lengthOfLIS(self, nums: List[int]) -> int:
  """
  The way to think of this is that you want to iterate backwards and find the longest increasing subsequence from that index to the end. As you keep moving
  backwards if you find a new number you can say that the LIS is your old answer plus 1 or the value that is already at your index.
  """
        ans = [1]*len(nums) #Every index is technically it's own LIS when we don't know anything since it can move to itself
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    ans[i] = max(ans[i],1+ans[j])

        return max(ans)
