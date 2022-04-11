class Solution:
    def minWindow(self, s: str, t: str) -> str:
      """
      Another doozy. First we start off by counting how any unique elements there are in our target string, t. We then initialize two variables to see how 
      many matches we have and how many we need while keeping a place to store all relevant information such as the amount of letters in t and the window
      we're looking at, the indices of the results, and the length of our result. We then start a sliding window approach. 
      
      We initialize a left pointer and have the right iterate. We add each character our right pointer sees to our window and we check to see if we need
      to update our have variable which will happen if the letter we just happened upon is in t and if the amount of characters in both hashmaps match.
      Have is a variable that stores the amount of matches. If the amount of matches we have is equal to the amount of matches we need we then need to
      iterate our left pointer. The strategy to do this is to move it until we no longer have all the variables you need to make matches. Aka you want a 
      new word window that doesn't meet the specifications of the problem. Doing this will give you the smallest window size that does meet the specifications
      If the smallest window size is less than your current minimum then update the result length and store the indices furthermore we need to update our left
      pointer. Since we're going to iterate it we need to decrement the letters count in the window dictionary and if it was a match we need to decrement it
      in our have variable. After all that we increment our left pointer. After getting all that we can pull the pointers we stored that have the indices 
      of the smallest windowsize and return them (the right pointer needs to get incremented by 1 since the indexing operation doesn't include the last index
      and we want the value at that index) but we need to check that the result length has changed from our default value otherwise return a blank string. Fin!
      """
        if t == "":
            return ""
        
        countT, window = {},{}
        
        for char in t:
            countT[char] = 1 + countT.get(char,0)
            
        have, need = 0, len(countT)
        
        res = [-1,-1]
        reslen = float("infinity")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #update result
                if (r-l+1) < reslen:
                    reslen = (r-l+1)
                    res = [l,r]
                #We want to move the left pointer    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        l,r = res[0],res[1]+1
        return s[l:r] if reslen != float("infinity") else ""
