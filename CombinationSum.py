class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      """
      Basically you want to keep track of your current index, the current list of numbers you have and the total sum of those elements. Basically you want 
      to look at each element and see if you should include it or not. So you append the current index to your list and run your recursive function on 
      the same index the new list of values (since you've appended the function already) and the sum which is the previous sum + the element added. Then 
      you pop the element and then call the same recursive function but this time you increment the function since in this recursive call you're not going 
      to include that element keep the current list of elements and the total the same. The base case is when the total equals the target then you append
      the list of elements to your global answer variable and if the total is bigger than the target or if the index variable is out of bounds you can just 
      return nothing. Finally you call your recursive function with 0, a blank list, and 0 and return your global answer function.
      """
        res = []
        
        def dfs(i,cur,total):
            if total == target:
                return res.append(copy.deepcopy(cur))
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)
            
        
        dfs(0,[],0)
        return res
