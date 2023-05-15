def validMountainArray(self, arr: List[int]) -> bool:
  """
  Basically you want to start a pointer at 0 and then check the conditions. The first loop is to go up the values so you 
  want to make sure that i is a valid index and arr[i] is less than arr[i+1] which is the condition of the ascending 
  mountain. If the pointer didn't move or we have reached the end of the list we can just return False right away since 
  we know that one side of the mountain will be missing. The next loop will be the same as the first loop except the 
  condition on arr[i] and arr[i+1] is reversed since we need to be going down the mountain. At the end, all we need to do is 
  check whether we have reached the end of the list. If we have we know we found a mountain.
  """
        n = len(arr)
        i = 0

        while i+1 < n and arr[i]<arr[i+1]:
            i+=1
        
        if i==0 or i==n-1:
            return False

        while i+1 < n and arr[i]>arr[i+1]:
            i+=1

        return i==n-1
