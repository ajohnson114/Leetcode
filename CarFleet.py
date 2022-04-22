class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      """
      You can look at each car as a vector and you want to see where each vector intercepts because if they intercept before the finish line then the one
      benaeth it will merge with the one in front of it. Each vector is parameterized by position and speed. We use a stack variable to track time to finish
      and add all the times after sorting by position and iterating backwards. If the time of a new car is less than or equal to that of a car that was added
      to the stack we know that they intersect and we can pop the most recent element as we know that the one we added before will be the speed they move at.
      This algorithm works for the entire list and all we need to do is return the length of the stack since that is all the cars who's stopping times weren't
      less than or equal.
      """
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)
