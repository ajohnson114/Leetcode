def lengthOfLIS(self, nums: List[int]) -> int:
  """
  You solve this by iterating backwards through the list and saying the length of the Longest Increasing Subsequence that starts at my index is 1 plus 
  the biggest of all the values in front of me if I'm smaller value than they are. The answer is the max of the answer array.
  """
        ans = [1]*len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    ans[i] = max(ans[i],1+ans[j])

        return max(ans)
        
