class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      """
      You want to loop backwards and compare the words you've come across to the words in your list. So you have 2 for loops: 1 going backwards through the
      list and the other going through the words in your dictionary. You need to check that the index even has enough space to allow for you to make the 
      word moving forward so you have to add the length of the word to your index to see if it's still valid and given that's true you also want to see
      that the index slice from i to the length of your word + i is equal to your word. If it is you know you can say that you can start here and form a 
      word that will help you solve the problem. Also you know that since you're moving backwards once you find a word that can be made you don't really 
      need to check that other words can be made from that index moving forward. Ex take leetcode if code can be found we set that value equal to true 
      then we iterate backwards and find that leet can be found too so we're finished.
      """
        dp = [False] * (len(s)+1)
        dp[-1] = True
        
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:len(word)+i] == word:
                    dp[i] += dp[i+len(word)]
                
                if dp[i]:
                    break
        
        return dp[0]
