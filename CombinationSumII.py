class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      """
      This is very similar to combination sum 1. This is backtracking where you want to choose to include the element run dfs on the rest of the list
      then choose to not choose that element and run backtracking on the rest of the list. You should sort the list because that will tell you where all 
      the duplicates are and you have an indicator varaible letting you know if you've seen the current element before. It's initialized to be -1 since
      you will never see a negative value in your list and then it's updated to be each element in the array so you know to skip this iteration if you've 
      seen duplicates. After you start iterating append your current number to your output array and run the backtracking algorithm on the next index,
      with the updated list with the target - your current number. Next pop from your current list and continue iterating. 
      
      Long story short you visit each element and decide whether to choose it and then go down the tree for each decision and see what your target is when
      you select all the numbers you select or don't select. You also keep track of your previous number so you know to skip it but it's basically a brute
      force approach
      """
        candidates.sort()
        
        res = []
        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
                
        backtrack([], 0, target)
        return res
