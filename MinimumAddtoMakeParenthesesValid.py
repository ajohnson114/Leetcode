class Solution:
    def minAddToMakeValid(self, s: str) -> int:
      """
      This makes some sense after you finish the problem imo. Basically you instantiate 2 variables minadd and balanced. You add 1 to balanced for every 
      open paren. you get because you are allowed to balance one more closing parethesis and you subtract one from balanced if balanced is greater than 0 
      and the element you're looking at is a closing parenthesis because you're taking up that closing position with a closing parethesis. The final case
      is that of a closing parenthesis with nothing to close it so we know that we must add one more opening parethensis for that unmatched closing one. 
      The answer is the unclosed open parentheses plus the unmatched closing parentheses.
      """
        if not s:
            return 0
        balanced = 0
        minadd = 0
        
        for i in s:
            if i == '(':
                balanced += 1
            elif i == ')' and balanced > 0:
                balanced -=1
            else:
                minadd += 1
        
        return balanced + minadd
