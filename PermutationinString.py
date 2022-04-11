class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      """
      This one is a bit tricky. So you want to compare the elements in two strings. To do that you can use a hashmap but here we have a list because it's
      a bit neater to query since we can figure out the index values based on ascii mappings. We start with an edge case. If s1 is longer than s2 then the
      problem is impossible. From there we initialize 2 blank arrays that will hold the initial letter counts of both s1 and the window the size of s1 in
      s2. From here we want to count how many of the index values match in both arrays (which is why we used arrays rather than dictionaries with a
      dictionary we'd have to have the alphabet to query i believe). We count matches if the index values of both arrays are equal meaning if both strings
      are missing an element that's a match. 26 means a perfect match since we know the window of letters we're looking at has all the letters in s1 and
      doesn't have all the letters that aren't in s1.
      
      After we compute our initial amount of matches we begin our two pointer approach. From here we look at our right pointer since that's what we're
      iterating with. We look to see the letter it's pointing at and we get the index of it in our s1count and s2count arrays by using ascii mapping
      (ascii represents char types as numbers: the lower case are conveniently consecutive numbers so we can get any mapping from 0-26 by doing
      ord(char) - ord('a') since 'a' is the first and smallest mapping). From here we know that the word window we're currently looking at has that 
      letter so we iterate the index in s2count and then we need to see what's happening with matches. If the updated s2count index now matches s1count's
      index we can iterate matches by 1 but if s2count's updated index value is bigger than s1count's index we know that we just lost a match. Similarly
      we now need to work with the left pointer since we plan on iterating it. We know we're shifting the left pointer so we lose one value of that index
      so we decrement that index value. Then we see if the updated index value matches s1count if it does we know that we found a match, if it doesn't we
      know we lost a match hence we decrement it. After doing this we can then iterate the left pointer and repeat the cycle. At the end of the loop we 
      can return True if matches is equal to 26 or False else because that's what we were looking for.
      """
        if len(s1) > len(s2):
            return False
        
        s1count = [0]*26
        s2count = [0]*26
        
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')] += 1
            s2count[ord(s2[i])-ord('a')] += 1
            
        matches = 0
        
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches +=1
        
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2count[index] +=1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2count[index] -=1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l +=1
            
        return matches == 26
                
            
            
