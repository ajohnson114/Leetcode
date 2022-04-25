class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      """
      The trick to this is to realize that you need to need to keep track of the current max and the current min and also need to reset those values when
      you see a 0. You need to track both in case you get a negative number. For instance [-1, -2,-3] the product of those 3 is -6 but if you were to add 
      one more negative such as -4 your answer would be 24. So your lowest minimum actually was necessary to compute that product. You need to include n 
      the number you're currently looking at in your maximum and minimum calculation in case your product gets reset (such as in the case of 0). So 
      basically loop through the values in the list, if the number is 0 reset the current maximum and current minimum values. Following that you want to
      update your current max to your the maximum of the previous current max * n, the previous current min *n and n itself. Those cases are mirrored in 
      the situtation when you update your current min but you will need to use a temporary variable that holds the value of the previous current max given
      you've just updated it. Finally the result is the bigger of the result and the current max
      """
        res = max(nums)
        currmax, currmin = 1,1
        
        for n in nums:
            if n == 0:
                currmax, currmin = 1,1
                continue
                
            tmp = currmax #you need the temporary variable since you will reset your current max and you still want the value of the previous one
            currmax = max(currmax*n,currmin*n,n)
            currmin = min(tmp*n,currmin*n,n)
            res = max(res, currmax)
        
        return res
            
            
