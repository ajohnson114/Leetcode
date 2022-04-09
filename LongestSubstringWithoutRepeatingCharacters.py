def lengthOfLongestSubstring(self, s: str) -> int:
  """
  The solution is best shown by looking at the test case: s = "abcabcbb" . We want to use a sliding window approach where we initialize 2 pointers
  that hold the maximum substring so far without a duplicate. To check if we don't have duplicates so far we use a set. When we find a duplicate we want
  to move the left pointer since we've checked all the cases that would contain the value at that index so far so we remove that value from the set 
  iterate the left pointer and add the value on the right (which will be the same value we just removed but it's nice for algorithmic understanding)
  and update the result (I believe it's r-l+1 since the length of the string is len(s) but the value of the last index is len(s)-1 so adding 1 gives us 
  the true answer. Finally we iterate the right pointer
  """
  
        charset = set()
        result = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            result = max(result, r-l+1)
            
        return result
