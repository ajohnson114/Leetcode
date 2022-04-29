class Solution:
    def reverseBits(self, n: int) -> int:
        """
        The algorithm in English:
        1. Do the following 32 times (because we have 32 bit integer)
        2. left shift res by 1
        3. add n%2 to res
        4. right shift n by 1"""
        
        res = 0

        for i in range(32):

            res = res << 1
            bit = n%2
            res += bit
            n = n >> 1

        return res
