class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      """
      Basically you want to push an open parentheses to the stack if the amount of open parentheses is less than n and push a closed parentheses to the 
      stack if the amount of closed parentheses is less than the amount of open parentheses and return it the stack if the amount of open and closed
      parentheses equals the total amount. You want to append and pop since you'll be using a recursive function on a global variable.
      """
        ans = []
        stack = []
        
        def backtrack(openN,closedN):
            if openN == closedN ==n:
                ans.append("".join(stack))
                return 
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
                
        backtrack(0,0)
        return ans
