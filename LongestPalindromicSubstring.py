class Solution:
    def longestPalindrome(self, s: str) -> str:
      """
      The trick is to not check to see if a word is a palindrome by reversing the string and iterating through it but to go to each index and expand 
      outwards. While the expanding word is a palindrome keep expanding. The other important thing to note is that there are two cases: one case where you 
      start at the index and expand outwards will lead to looking for odd palindromes and the other that you have to remember to add is that of even 
      length palindromes where you will have to start on different indices. From there you set a while loop to check that your pointers are in bounds and 
      the word is a palindrome and check to see if the palindrome you found is bigger than the length of the previous ones. If it is you found a new biggest
      then increment your pointers and continue the loop.
      """
        res = ''
        reslen = 0
        
        for i in range(len(s)):
            #Odd palindromes
            l,r = i , i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = (r-l+1)
                l -= 1
                r += 1
            
            #Even palindromes
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = (r-l+1)
                l -= 1
                r += 1
            
        return res
            
