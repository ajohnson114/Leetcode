class Solution:
    def validUtf8(self, data: List[int]) -> bool:
      """
      This I feel is a pretty poor question. Basically to start you want to count the amount of bits in a number. Having all 0's is fine so we can just go 
      to the next element in the loop for this if we want. Next we need to check if 10 is the starting bit configuration because that is invalid so we check
      to see if count ==1 or if it is greater than 4 so we can return False and then decrement our counter. Honestly I don't really understand the question
      and I think one might just want to remember the solution
      """
        def countOnes(num):
            count = 0
            for i in range(7, -1, -1): # 10000000 = 1 << 7
                if num & (1 << i):
                    count += 1
                else:
                    break
            return count
        count = 0
        for d in data:
            if not count:
                count = countOnes(d)
                if count == 0:
                    continue
                if count == 1 or count > 4:
                    return False
                count -= 1
            else:
                count -= 1
                if countOnes(d) != 1:
                    return False
        return count == 0
