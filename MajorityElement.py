def majorityElement(self, nums: List[int]) -> int:
  """
  This is something I solved in Sheffer's class. Basically you start at the first element, set it as the leader and say that it has appeared
  once. The premise is that the leading element has appeared more times than any other element so if we increment it everytime it shows up
  and decrement a leader when it doesn't match the other element the one that appears the most should win out.
  """
        leader = nums[0]
        count = 0

        for i in nums:
            count +=1 if i==leader else -1
            if count <0:
                leader = i
                count+=1
        
        return leader
