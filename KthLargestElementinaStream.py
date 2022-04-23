class KthLargest:
  """
  You want to use a minheap and store the k biggest values. So you instantiate minheap by taking the array and calling the function heapq.heapify(array)
  the heappop while the length is larger than k. When you add an element you want to push it onto the heap with heapq.heappush(heap,value) then check to see
  the length of the minheap is greater than k because you will need to heappop again. Finally return the smallest value in the heap which is at the 0th 
  position
  """
    def __init__(self, k: int, nums: List[int]):
        #minheap with k elements
        self.minheap, self.k = nums,k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
