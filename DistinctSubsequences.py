def numDistinct(self, s: str, t: str) -> int:
  """
  s is the string with extra characters and t is the string we want to find the matches for
  
  Solve with dfs!
  
  We want to go down t and see how many ways we can match the characters in s and t. To do this we generally want to go down every
  index in s and t. If the characters at that point match, then we can increment both pointers and run the same operation for the next
  2 values but we'd also like to see if the next index in s will match the current index in t so we also run the function where we just 
  increment the pointer in t. So practically this looks like dfs(i+1,j) + dfs(i+1,j+1) where i and j are the pointers for t and s 
  respectively. If they don't match we just need to move on to the next element in t which looks like dfs(i+1,j). We know that we can 
  stop the functions because we will have matched all the letters in t which means that we can then return 1 and the other stopping case
  is that we reached the end of our word s in which case we would return 0. Finally we introduce caching to the function and we have our
  solution. Cheerio!
  """
        dp = {}

        def dfs(i,j):
            if j == len(t): 
                return 1
            if i == len(s): 
                return 0
            if (i,j) in dp: 
                return dp[(i,j)]

            dp[(i,j)] = 0

            if s[i] == t[j]:
                dp[(i,j)] += dfs(i+1,j) + dfs(i+1,j+1)
            else:
                dp[(i,j)] += dfs(i+1,j)
            return dp[(i,j)]
        
        return dfs(0,0)
