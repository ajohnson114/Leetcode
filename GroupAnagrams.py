def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
  """There is a different solution than this one which involves sorting and grouping by the set of characters that are there but that's apparently not 
  optimal based on time complexity since it is O(m*n*logn) where m is the average length of the characters and n is the amount of strings. This is
  O(m*n*26) (constants get dropped) but uses a bit more memory if I remember correctly. Here you make a mapping from the characters in the string you're 
  looking at and compare them to the mapping of all the otherr strings. If they share the same mapping they are anagrams. You find the mapping with 
  0-based indexing by taking the ASCII values and subtracting that of 'a' since it will have the smallest ASCII value. We use a defaultdict to ameliorate
  the edge cases. Arguably this isn't the best way spacewise but all in all it seems fine.
  """
        res = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] +=1
                
            res[ tuple(count)].append(s)
        
        return res.values()
