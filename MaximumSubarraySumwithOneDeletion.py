class Solution:
    def maximumSum(self, arr: List[int]) -> int:
      """
      You want to figure out what the biggest subarray is at the index you're currently at with that element deleted and without it being deleted and then
      find the maximum of those two. So you create 3 variables, big which is the biggest element you've seen so far, prenotdeleted which is the biggest sum 
      with the previous element not deleted and prewithdeleted which is the biggest sum with the previous variable deleted. You initialize prenotdeleted to
      arr[0] because you intend to start at the second element and prewithdeleted to 0 since you will start at the first element and pretend you deleted the 
      first. The biggest you've seen so far will then be the first element. Prewithdeleted will be updated to the maximum of prenotdeleted and 
      prewithdeleted+arr[i] because you can either keep the previous sum of all the integers that weren't deleted and delete this one or delete one of previous
      ones and add this one. Prenotdeleted is the running sum of all elements if they're not negative. Curr is the current biggest sum and we want to compare 
      that to the biggest sum we've seen so far which is stored in the variable biggest. Finally we return the biggest subarray, which is our variable big. 
      """
        prenotdeleted = arr[0]
        prewithdeleted = 0
        big = arr[0]
        
        for i in range(1,len(arr)):
            prewithdeleted = max(prenotdeleted, prewithdeleted+arr[i])
            prenotdeleted = max(prenotdeleted+arr[i], arr[i])
            curr = max(prewithdeleted, prenotdeleted)
            big = max(big,curr)
            
        return big
