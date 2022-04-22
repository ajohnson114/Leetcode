class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      """
      Basically store each value and index in a stack as they come in and when you find a value bigger than the top of the stack pop until there's nothing
      smaller than the value you're looking at in the stack and for each one set the value in the answer equal to the difference of their indices. After 
      you can't find smaller elements append the value and index pairing to the stack and continue the process. If you can't find anything that's ok since 
      you initialized everything to 0 anyway.
      """
        ans = [0] * len(temperatures)
        stack = []
        
        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                popval, popidx = stack.pop()
                ans[popidx] = idx - popidx
            stack.append([val, idx])
        
        return ans
