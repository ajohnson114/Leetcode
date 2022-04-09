class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
"""      
This uses an algorithm called bucket sort. You initialze a blank array of size len(nums) because you are going to count the number of keys that occur
that index number amount of times. We initialize the values to be blank lists because we are going to append all numbers that occur that many times
into the list. The dictionary is used to count the amount of occurences initially. Once we have all the initial counts, we put all the keys that occur
that many times into the count[value] list. From there we iterate backwards through the count list (the list of lists) and add k elements to an 
answer list.
"""      
        dict_ = {}
        count = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            dict_[i] = 1 + dict_.get(i,0) #.get() gives us the value associated with the key (first parameter) and specifies a value to return if nothing
            #exists
            
        for n,c in dict_.items(): #.items() returns (key,value) pairings
            count[c].append(n)
            
        result = []
        
        for i in range(len(count)-1,-1,-1):
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result
