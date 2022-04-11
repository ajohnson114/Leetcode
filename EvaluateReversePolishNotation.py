class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      """
      This uses a stack. Basically you store the numbers as you get them, when you get an operation if the operation is commutative pop twice and append
      the result. Otherwise store the last 2 variables from the stack in variables (by popping twice) and perform the operation. You're guaranteed to 
      always get a number that evaluates to something so you just have to return the 0th element in the stack since there will always only be one.
      You also need to truncate division and round down and the int() function in python does that automatically which is nice.
      """
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
                
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
                
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
                
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append( int(b/a) )
                
            else:
                stack.append(int(i))
        
        return stack[0]
