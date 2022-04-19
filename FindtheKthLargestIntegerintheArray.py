class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
      """
      There is an implementation of this that uses quick select that has an optimal time complexity O(n) but has a worse worst case scenario O(n^2). This 
      has a theta(klogn) time complexity which means that the best and worst case is klogn which is a decent tradeoff in my opinion. The trick is to convert
      the list to a heap and since python doesn't have max heaps we will make a max heap out of the built in min heap by making everything negative. So 
      we make an array of all the negative numbers and then we make a heap and pop k-1 times. We then return what is on top of the heap since that will be 
      the next to get popped and will be the answer to our question. 
      """
        maxHeap = [-int(i) for i in nums]
        heapq.heapify(maxHeap)
        
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
            
        return str(-maxHeap[0])
