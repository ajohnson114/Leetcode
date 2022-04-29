class Solution:
    def hammingWeight(self, n: int) -> int:
      """
      The trick to this is to bitwise and the number with 1 and then bitshift it. When you & it with 1 you will see that everything gets 0'd out except for
      the bit in the first position and you are left with 1. If this is the case then you can increment your count of bits by 1. After checking this you 
      can bitshift your number to the right by 1 and then do repeat the process. It's a 32 bit number so do this 32 time and return your answer.
      """
        count = 0
        for _ in range(32):
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count
