def reverseString(self, s: List[str]) -> None:
"""
Basically we just take a 2 pointer approach, switch the values and increment the pointers
"""
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s)-1
        
        while low < high:
            s[low], s[high] = s[high], s[low]
            low+=1
            high-=1
