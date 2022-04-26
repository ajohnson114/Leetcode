class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      """
      You're making a (len(text1) + 1) * (len(text2) + 1) grid where each ij point will represent whether the word's at that point share an intersection
      If they do share an intersection at that ij point we can say that dp[i][j] is equal to dp[i+1][j+1] + 1 since we can sort of move both pointers
      so to speak (I'm saying that out of convenience of visualization) otherwise we have to check to what would happen if we checked the subproblem of
      incrementing each word by 1 and comparing it the other word. In other words check text1[i+1] == text2[j] and text1[i] == text2[j+1]. This is done
      conveniently by taking the max of dp[i+1][j] and dp[i][j+1]. Finally we return dp[0][0] since we're iterating backwards through the words.
      """
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
            
        
