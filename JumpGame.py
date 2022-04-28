class Solution:
    def canJump(self, nums: List[int]) -> bool:
      """
      You have a goal post that you want to reach which is your last index. When you know that you can reach your goal from one index all you need
      to do is slide your goal back to the index you just saw that you could reach the index you were just at from a previous index so you can just 
      slide your goal back. This works because if you can reach the place you just saw that you could reach the last index from you can go to this
      place and from there go to the last index. Then the problem reduces to whether or not you can reach the places where you can reach your last
      index and all in all you want to see if you can reach those places from your starting point. 
      """
      
        goal = len(nums)-1
        
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
