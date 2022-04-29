class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      """
      This is very similar to the original subset problem. The difference is that here you have to skip over duplicates with a while loop.
      So you find all the branches of backtracking with each index and you find all the branches without that index while realizing that any duplicate 
      branches will be computed by one of your original backtracking calls since you're always running the algorithm on two versions: one with the element
      and one without. You should probably draw a branching diagram.
      """
        res = []
        subset = []
        nums.sort()
        
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::]) #append everything in subset to your result
                return 
            
            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, subset)
        return res
