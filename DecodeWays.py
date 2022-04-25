class Solution:
    def numDecodings(self, s: str) -> int:
      """
      You can solve this with either a recursive dfs or a dynamic programming approach. For each number we know that we can decode it in one of two way.
      We can take it as an individual or we can take it as a collective with the next number. The first case is simple but the second case is a bit more 
      interesting. Given that these are letters of the alphabet we can only take a number if it is between 1 and 26. Furthermore, the problem specifies
      that we can't have a leading 0 count for our algorithm. So we know that our result is the amount of mappings our index or our index plus the next one
      has plus all the mappings of those before that one. We know that 0's cant be mapped to anything else so the answer to that one is 0.
      """
      
      #Recursive Solution
        dp = {len(s):1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)
            
            if (i +1 < len(s)) and (s[i] =="1" or s[i] == "2" and s[i+1] in "0123456"):
                res += dfs(i+2)
            
            dp[i] = res
            
            return res
            
        return dfs(0)
            
      
      dp = {len(s):1}
      for i in range(len(s)-1,-1,-1):
        if s[i] == '0':
          dp[i]=0
        else:
          dp[i] = dp[i+1]
       
        if (i +1 < len(s)) and (s[i] =="1" or s[i] == "2" and s[i+1] in "0123456"):
          dp[i] += dp[i+2]
     
      return dp[0]
          
        
          
            
