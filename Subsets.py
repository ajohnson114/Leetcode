class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      """
      You want to make a recursive function where you inlude the current index you're looking at and then call the recursive function and then you exclude
      that index and then call the function again. The base case is that the index is out of bounds. To get the answer call the recursive function on the 
      root and then return your answer
      """
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(copy.deepcopy(subset))
                return 
            
            #decision to include
            subset.append(nums[i])
            dfs(i+1)
            
            #decision to not include
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        
        return res
            
