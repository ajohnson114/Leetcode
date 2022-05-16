class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      """
      You want to sort by the starting times of all the meetings. and then compare the ending time to the last ending time we added to our output array. 
      For this to work we need to instantiate our output array with the first element after sorting in there. If our current starting time is 
      smaller or equal to our last ending time then we can say that our ending time of the last element in the output array is the bigger of the last ending
      time and our current ending time. Otherwise, we can just put the new interval into the array. Finally we can just return our answer array
      """
      
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]
        for start, end in intervals[1:]:
            lastend = ans[-1][1] 
            if lastend >= start:
                ans[-1][1] = max(lastend,end)
            else:
                ans.append([start,end])
        
        return ans
            
            
