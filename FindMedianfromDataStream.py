class MedianFinder:
  """
  The key to solving this question is realizing that you need to use a heap (2 acutally). You want to have a small heap and
  a big heap, all elements in the small heap are smaller than all elements in the big heap. The small heap will be a max
  heap and the big one will be a min heap because if we want to get the median of the stream we need to get can think of 
  it as the value that creates 2 even partitions of a sorted array (which is what our heaps represents) in the even case 
  we need to take the maximum of the small heap and the minimum of the big heap and divide by 2 and in the odd case we would
  want to take the (min or max) value of the heap with an odd amount of elements and return
  
  So for this we add every element that comes in to the small (max) heap. Then we check to see that the number that came in
  is smaller than all the elements in the large (min) heap and if it's not we pop the biggest element from the small heap
  and add it to the large heap. Then we check to see if one heap is getting too large (more than a size difference of 1) and 
  if it is, in the case where the small heap is bigger we take the biggest element and put it in the large heap and in the
  other case we do the opposite. Finally, in the find median function we check to see if the size difference is present and
  if it is we return the min or max of the one that is bigger. Otherwise, if they're even we take the biggest and the smallest
  divide by 2 and return our median
  """

    def __init__(self):
        self.small = [] #max heap
        self.large = [] #min heap
       
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num) #we add every # that comes in to the small heap first
        #make sure that every element in small is <= min(large)
        if (self.small and self.large \
        and (-self.small[0]) > self.large[0]): #if every element in small is <= min(large) we pop the biggest element and
            val = -heapq.heappop(self.small) #move it to the other heap
            heapq.heappush(self.large,val)
        
        if len(self.small) > len(self.large)+1: #if the amount of elements in the small heap are more than 2 the amount of 
            val = -heapq.heappop(self.small) # elements in the big heap we want to pop the biggest from the small heap and 
            heapq.heappush(self.large,val) #move it over
        elif len(self.small)+1 < len(self.large): #we do the opposite of the above comment
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): #if the total amount of elements is odd and small has the extra number
            return -self.small[0] #we return the biggest from small
        elif len(self.small) < len(self.large): #if the total amount of elements is odd and large has the extra number
            return self.large[0] #we return the smallest from small
        else:
            return (self.large[0] + -self.small[0])/2 #if it's even we take the biggest from small and smallest from large
          #and divide by 2
