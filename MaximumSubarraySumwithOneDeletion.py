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
      
      Better explanation: You are running kadane's algorithm twice in place in the for loop. prenotdeleted is kadane's algorithm as you want to see if you
      can add up all the numbers before this one and get a bigger sum. If you can keep going otherwise (you'll have a negative number and be subtracting)
      stop the loop. Prewithdeleting is a value that sees what would happen if I deleted one of my previous elements and added this one to see if it would
      be bigger than the biggest contiguous sum possible while keeping all of my elements. The bigger of the two is clearly the answer to the problem. Big
      is a placeholder for the biggest value we've seen so far so we don't have to call max at the end of the loop and curr is the biggest sum at the 
      current index
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
