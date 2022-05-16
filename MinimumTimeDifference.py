class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
      """
      This I feel self documents in a way. We convert all the timestamps to a minute representation (there are 60*24 minutes in a day). If there are 1440+
      minutes we return 0 since we will have the same number twice by pigeonhole. Then we sort the numbers and take pairwise differences since they will
      have the shortest difference and find the lowest minimum we've seen so far. Finally since we have a 24 hour clock the last time and the first time 
      could be the closest so we compare the modulo 1440 of the first minus the last since that will give us the remainder after division. Then finally
      we can return the minimum.
      """
        def toMinFromZero(t):
            return 60*int(t[:2]) + int(t[3:])
        
        maxMins = 60*24 # number of mins in a day
        if len(timePoints) > maxMins:
            return 0
    
        # we sort the timestamps. Idea: The smallest difference will always be a 
        # difference between two neighboring times in the array.
        ts = [toMinFromZero(t) for t in timePoints]
        ts.sort()
        
        diffMin = maxMins
        # calculate the pairwise difference ...
        for i in range(1,len(ts)):
            t_high = ts[i]
            t_low = ts[i-1]
            diffMin = min(diffMin, t_high - t_low)
        # ... and due to the 24 hour clock, don't forget the last and first entry with modulo arithmetic
        diffMin = min(diffMin, (ts[0] - ts[-1]) % maxMins)
        
        return diffMin
