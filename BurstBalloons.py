def maxCoins(self, nums: List[int]) -> int:
  """
  time = O(n^3) space = O(n^2)
  The question presents the problem to you as you bursting (popping from the array) and then multiply as they go out. That
  leads you to think about what would happen if that balloon were the first one popped but the key to solving this problem 
  is to think what would happen if that balloon were the last one popped. From this perspective, we can run two subproblems 
  on the subarray to the left of the index and the subarray to right of the index.
  
  So for our dfs function is the pointers cross we return 0 and if the value is already calculated we return the cache of it
  Then we set the cache value to 0 initially then we loop through the remaining array and do our original bubble burst 
  calculation nums[i - 1] * nums[i] * nums[i + 1] where it is now nums[l - 1] * nums[i] * nums[r + 1] since i is the last
  one to be popped we store this to coins and then to that we add the answers to the subproblems which is now the left 
  subarray minus the index so dfs(l,i-1) and the new right subarray dfs(i+1,r). Then we cache the calculated value if it
  is bigger than our already calculated cached value and then return the answer in the dfs function. Finally we can, 
  just call the dfs function. Note we added one to the ends of the problem since the problem specified it that way so
  to fix our indices we should call the function on the original boundaries of 1 and len(nums)-2
  """
        nums = [1]+nums+[1]

        dp = {}

        def dfs(l,r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = 0

            for i in range(l,r+1):
                coins = nums[l-1]* nums[i] * nums[r+1] #original bubble burst calc
                coins += dfs(l,i-1) + dfs(i+1,r) #the problem on the left and right subarrays
                dp[(l,r)] = max(dp[(l,r)], coins) #cacheing

            return dp[(l,r)]

        return dfs(1,len(nums)-2)
