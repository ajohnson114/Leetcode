class Solution:
    def isValid(self, s: str) -> bool:
      """
      The key to solving this is by using a stack. We know that parentheses must be closes immediately so we can initialze a dictionary with keys as closing
      parentheses and values as open parentheses. Then we iterate through the string and append all the open parentheses and check if the value we're 
      currently on is a closing parenthesis. If it is we should check that the stack isn't empty and it is closing something and that the thing it is closing
      is its corresponding pair which we can check by querying the dictionary we made. Thats it!
      """
        close = {')' : '(' , '}':'{', ']':'['}
        paren = []
        for i in s:
            if i in close:
                if paren and paren[-1]==close[i]:
                    paren.pop()
                else:
                    return False
            else:
                paren.append(i)
        return True if not paren else False
