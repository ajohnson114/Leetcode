def diStringMatch(self, s: str) -> List[int]:
  """
  This is a super confusing prompt tbh. Basically you want to guarantee that you can always find a number bigger and 
  one that is always smaller. To do this we set 2 pointers as 0 and the other as len(s) since the range is n+1 in the 
  problem. So now we can iterate through the array and if we find an "I" we know that we need to find a number smaller
  than the one next to it so we can append the lower pointer to answer and then increment the pointer, in this scenario
  we know that l++ will be bigger than the original l and r will always be bigger than l. In the other case, we can
  append the right pointer and then decrement it since we need to find a number that will be smaller than the previous one
  and we know that r-- will be smaller than the previous r and l is smaller than r. We know that we will get n commands
  with respect to so we have 1 number left over. In this problem, l will always have the left over number so we add that to
  our answer and return.
  """
        l,r = 0,len(s)
        ans = []

        for char in s:
            if char == 'I':
                ans.append(l)
                l +=1
            else:
                ans.append(r)
                r-=1
        
        return ans+[l]
