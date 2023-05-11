def strStr(self, haystack: str, needle: str) -> int:
  """
  Basically loop through the positions of the haystack the needle can start from and check to see if from that point on you can form
  the needle. If you can return the index if not return -1. 
  """

        if not needle:
            return 0

        for i in range(len(haystack) +1 -len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
        
        
        
        """n = len(needle)
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i+n] == needle:
                    return i
        elif needle not in haystack:
            return -1
        return 0
        
        return -1"""
