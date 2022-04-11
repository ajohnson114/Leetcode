class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      """
      Sliding Window. Start a pointer at the beginning of the string and a second pointer that will iterate through. Create a hashmap to store counts of all 
      the characters you see so far and a variable to hold the biggest count. As you iterate through with your right pointer you want to make sure that your
      window of characters is still valid. You can do this by checking the window size in comparison to highest letter amount since you know that you
      want all your minority letters to be changed to the majority letter (in theory which is why we have k because we can change k of them). While the 
      size of the window - the amount of the majority letter is bigger than k we have an issue since we have rogue letters that we can't convert to the 
      majority. Therefore we increment the left pointer and make the window size smaller while the window size - amount of majority letter > k. While 
      doing this we need to remember to decrement the count of the letter we're taking out in the hash map. Finally we just return the variable that was 
      supposed to hold the largest window size.
      """
        l = 0
        most = 0
        letters = {}
        
        for r in range(len(s)):
            letters[s[r]] = letters.get(s[r],0) + 1
            
            while (r-l+1) - max(letters.values())>k:
                letters[s[l]] -=1
                l+=1
                
            most = max(most,r-l+1)
            
            
            
        return most
