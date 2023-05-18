def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        
        The trick used to solve this is to transpose the input: 
        strs = ["abc", "def", "ghi"]  list(zip(*strs)) = [('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i')]
        Then you iterate through list(zip(*strs)) and see if the length of the set is equal to 1 and if it is then we 
        append to the result and if it's not we break as the prefix is now different. At the end we just join the prefix
        
        Note: the zip function will stop making tuples when there isn't an equal amount of things to join i.e. it stops
        at the length of the shortest word in this case. For instance the following will have the same output as above
        strs = ["abc", "defz", "ghiy"]  list(zip(*strs)) = [('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i')]
        
        """
        prefix=[]
        num = len(strs)
        
        for x in zip(*strs): #this line transposes the input
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix) 
