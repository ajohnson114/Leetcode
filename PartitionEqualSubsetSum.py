class Solution:
    def canPartition(self, nums: List[int]) -> bool:
      """
      This can be partitioned into two sets if the sum is even and the target for a subset we'll be looking for is sum(nums)/2. The basic idea of this 
      algorithm is to start off with 0 in a set and then add each successive integer to all the previously computed sums in the set. Iterating forward 
      or backwards doesn't really matter here. For the case [1,5,11,5] assuming we're iterating backwards we add 5 to the set so we have {0,5} in the 
      set. On the next iteration, we repeat the process and get {0,5,11,16} then we do this again with 5 and get {0,5,10,11,16,21} and again with 1 and get
      {0,1,5,6,10,11,12,16,17,21,22} along the way in our algorithm we can check to see if nums[i] + the value in our set is equal to the target and if 
      it is we can return True. Otherwise we return False.
      """
        if sum(nums)%2==1:
            return False
        
        dp = set()
        dp.add(0)
        
        target = sum(nums)/2
        
        for i in range(len(nums)-1,-1,-1):
            nextdp = set()
            for t in dp:
                if t+nums[i] == target:
                    return True
                nextdp.add(t)
                nextdp.add(t+nums[i])
            dp = nextdp
        
        return True if target in dp else False
