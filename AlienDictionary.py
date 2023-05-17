def alienOrder(self, words: List[str]) -> str:
  """
  This is tricky until you see the trick and then it's just courseScheduleII with a post order dfs.
  The trick is that you have to sort of think about how a computer tells how to sort 2 words. It does so by comparing 
  each position of the strings and then finding the first element that is different and then seeing which comes first in
  the dictionary and then putting the one that comes first first. BOOM. So now that's how we're going to build our adjacency
  list (Graph). 
  
  We initialize a set for each character that appears in the word list. Then we iterate through the list comparing words
  we search the characters the words share and if the first word is bigger than the one we're comparing it against 
  and they share the same prefix we return an empty string otherwise we loop through the first word to find the element that
  is difffernet in the first word. When we find the element that is different in the first word we add the character that is 
  different in the second word to the adjacency list of the first word. From here we just need to do a post-order DFS.
  A post order DFS is basically when you run a DFS but you add the node you ran the DFS on to the result at the end of the 
  function call.
  
  So now we initialize a visited dict and a result variable. The visited dictionary will hash the character and then a boolean
  .Here False will say that we have visited it and True will say that we have added the character to the path. This is important
  since we're doing a post-order BFS. Then create a dfs function. The base case is if the character is in visited we should return
  the value of the character in the visited set. After the base case we initialize the value of the character to True 
  then loop through all the neighbors in the characters adjacency list. If any of those return True we should return True too
  Finally we set the visited value equal to false to say that it has been visited and then append the value to the result.
  
  Now our dfs is done and we can run dfs on every character in the adjacency list.  If any of them return True we can return
  an empty string and if that doesn't happen we can reverse the result list and then return the joined answer.
  """
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
