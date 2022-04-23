class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      """
      Basically you want to create a recursive function where you do the brute force work. You traverse down the rabbit hole till you get to the cases of 
      each element being on their own and then you add the previous elements to the end of their list and then send that list back up the chain. This is 
      pretty hard to explain at the moment but draw out the tree diagram and do the flowchart. You pop the first element then run the same function on 
      the rest of the list. From there you repeat until you get to the base case. That number will have the other number appended to the end and in the case
      where number you just appened is the single list the number you just appended to will be appened to that number. All that goes back uphill until you
      you to extend the permuatations just found to your result and then append the first element to the result again
      """
        res = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
                
            res.extend(perms)
            nums.append(n)
        
        return res
                
        
