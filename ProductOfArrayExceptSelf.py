def productExceptSelf(self, nums: List[int]) -> List[int]:
  """
  This is a suboptimal solution and what it does is that it initializes 2 arrays that will hold the product of everything to the right of that index
  and the product of everything to the left of that index and then it multiplies it together. There is a way to do this all with a single array though.
  This is my first guess code that I thought of off the top of my head.
  """
        a, b = [1] *len(nums), [1] *len(nums)
        
        for i in range(1,len(nums)):
            a[i] *= nums[i-1] * a[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            b[i] = nums[i+1]*b[i+1]
            
        ans = [a[i]*b[i] for i in range(len(nums))]
        
        return ans
      

      
      
def productExceptSelf(self, nums: List[int]) -> List[int]:
  """
  This is an optimal approach that only uses 1 array rather than 2. We start with prefix and postfix values (initialized to 1 since we want to iterate on 
  the list) then we go forward though the list and assign the value of the prefix to the answer list first and then multiply the prefix by the current #.
  This has the same effect as the above first for loop. Then we work backwards through the list and do the same as the previous loop. The resulting array
  is our answer.
  """
  
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
