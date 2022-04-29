class Solution:
    def isHappy(self, n: int) -> bool:
      """
      Create a variable to hold your answer and after that iterate through your number (as a string because it's python) and square all the integer values
      you find. Once you loop through all the numbers check to see if you've seen that number before because if you have then you are stuck in a cycle and
      must return False otherwise add the number you've just seen to your list and then repeat your process by iterating by the new sum of squares. If you
      reach 1 return True
      """
        ans = [n]
        while n != 1:
            res = 0
            for i in str(n):
                res += int(i)**2
            if res in ans:
                return False
            n = res
            ans.append(res)
        return True
