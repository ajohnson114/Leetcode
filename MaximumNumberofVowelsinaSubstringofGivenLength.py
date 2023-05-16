def maxVowels(self, s: str, k: int) -> int:
  """
  At first I tried this one myself and knew it was a 2 pointer solution but didn't figure out the specific implementation
  but its pretty simple. We set up an array of vowels, an answer variable we start at 0 (vows), 2 pointers (i and j),
  and a counter variable (c). We then loop while the right pointer is less than the length of the word and say that if
  the left pointer minus the right pointer is less than k then if the right pointer is a vowel we increment the counter
  and increment the right pointer regardless of if the pointer was a vowel or not. If the distance between the pointers is 
  not less than k we check to see the left pointer is a vowel, in the case that it is we decrement the counter, and increment
  the left pointer regardless of whether it's a vowel or not. Then we compare the counter to the answer variable and 
  assign the answer variable to the max of both. At the end we just return the answer variable
  """
        vowels = ['a', 'e', 'i', 'o', 'u']
        vows = 0
        n = len(s)
        i = 0
        j = 0
        c = 0
        while j<n:
            if j-i<k:
                if s[j] in vowels:
                    c+=1
                j+=1
            else:
                if s[i] in vowels:
                    c-=1
                i+=1
            vows = max(vows, c)
        return vows
