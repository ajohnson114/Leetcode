class Solution:
    def countBits(self, n: int) -> List[int]:
      """
      The idea here is that the number of 1 bits in some num i is: 1 if the last digit of i (i % 1) is 1, plus the number of 1 bits in the other digits 
      of i (ans[i // 2]). (Ex. 0 -> 0 + 0 1 -> 0+1  2 -> 1 (from last Ex) +0 3-> 1 (from 1) + 1 =2 and so on and so on)
      """
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i & 1)
        return ans
