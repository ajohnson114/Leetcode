def climbStairs(self, n: int) -> int:
  """ Fibonacci Sequence"""
        arr = [1,1]
        while len(arr) < n+1:
            arr.append(arr[-1]+arr[-2])
        return arr[n]
