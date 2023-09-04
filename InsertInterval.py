def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
  """
We initiate a blank array and start a for loop in the loop there are basically 3 cases since the intervals are sorted:
1) If the interval you're looking at in intervals has a end that is sooner than the start of your new interval you can just add it to the answer since it is before the new interval
2) If the new interval has a smaller end than the start of the current interval you can just add the new interval to the answer and then add the rest of the list to the answer
since we know that it is sorted and we just said that the current interval starts after our new interval so the rest of them do too
3) Finally if there is some overlap between the two intervals we want to update new interval to the min of the starting times and the max of the ending times.

If we exit the for loop we know that nothing is returned which means that the answer array has no intervals in it and one can think further that there were no intervals that were
important. Which means that we can add the new interval to the answer and return it
  """
        ans = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
        
        
        ans.append(newInterval)
        return ans
