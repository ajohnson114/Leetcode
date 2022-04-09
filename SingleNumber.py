def singleNumber(self, nums: List[int]) -> int:
  """Xor the number with 0 all the bits will cancel themselves out and leave the unique number"""
        a = 0
        for i in nums:
            a ^= i 
            
        return a
