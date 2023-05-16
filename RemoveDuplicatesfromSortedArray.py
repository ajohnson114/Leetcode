def removeDuplicates(self, nums: List[int]) -> int:
  """
  Basically, this is a 2 pointer problem. We start the right and left pointers at the second index (1) and then check to see
  if the pointer we're at is equal to the one before it. If it is we continue but if it's not we set the value at the left 
  pointer equal to the value at the right pointer and then increment the left pointer and then keep looping the right pointer.
  At the end of this procedure we will return the left pointer as that will contain the answer
  
  """
        l=1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[l] = nums[i]
                l+=1
        return l
