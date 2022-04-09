def findLengthOfLCIS(self, nums: List[int]) -> int:
"""
I iterated backwards through the list and said that the the longest continuous increasing subsequence that starts at this index is 1 plus that of the 
person in front of me if im smaller than the value at the index in front of me. The solution is inspired by Dynamic Programming.
"""
        ans = [1] * len(nums)
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                ans[i] = max(ans[i], ans[i+1]+1)
                
        return max(ans)
