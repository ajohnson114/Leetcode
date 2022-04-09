def findDuplicate(self, nums: List[int]) -> int:
  """
  Problem: Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

  There is only one repeated number in nums, return this repeated number.

  You must solve the problem without modifying the array nums and uses only constant extra space.
  
  Solution: This is a linked list problem. The numbers are in the range [1,n] and there is a cycle. There really isn't an intuitive way to solve it 
  so you just have to learn Floyd's algorithm. The simple explanation is that we know index 0 will never be part of the cycle and that the numbers at
  the other indices will point to another place in the cycle. So Floyd's algorithm says that we should initialize 2 pointers, one fast and one slow. 
  We will iterate the fast pointer twice along the linked list on each iteration and the slow once. When they intersect, we break and then we will
  start another slow pointer at index zero and iterate it along with the old slow pointer. There's a proof that says the distance from where the pointers
  will intersect to the start of the cycle and the origin to the start of the cycle is the same but those details are a bit much for this. 
  Therefore, when the new and old slow pointer intersect you will be at the start of the cycle and it will be the solution!
  """
        slow,fast = 0,0
        
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while 1:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
