def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        
        The trick used to solve this is to transpose the input: 
        strs = ["abc", "def", "ghi"]  list(zip(*strs)) = [('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i')]
        Then you iterate through list(zip(*strs)) and see if the length of the set is equal to 1 and if it is then we 
        append to the result and if it's not we break as the prefix is now different. At the end we just join the prefix
        """
        prefix=[]
        num = len(strs)
        
        for x in zip(*strs): #this line transposes the input
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix) 
