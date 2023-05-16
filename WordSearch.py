def exist(self, board: List[List[str]], word: str) -> bool:
  """
  For this you want to do a dfs as you would generally want to do with a matrix problem. So what happens is the dfs fcn 
  takes in the position on the board and the index you're currently comparing the board position to to the index in the 
  word. So we set up the positions we will consider next with a directions array and we keep track of the positions we've
  visited with a visited set. So with the dfs function we first want to check if i is equalt to the length of the word
  which means in that case we've found the word so we should return True. Then we check to see if the the position is valid,
  the board position we're at matches the currently found index, or we've already used this letter in the function.
  After this we use the position so we add it to the visited set, we create a flag variable that we set initially to false,
  then we traverse all the directions and increment the pointer in the word and call the function on all the positions. If
  any of those function calls return True we set the flag equal to true. After the loop se then remove the position from the
  set and return the result variable. Something that we add for the sake of getting the code to pass Leetcode's time 
  restriction is to reverse the word if the first letter appears more times than the second letter.  I don't know why that
  works but it apparently does so it's implemented here. We then loop through the matrix and see if the function returns True
  and if it does we return True. After that loop if it doesn't return True we then return False.
  """
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()

        def dfs(x,y,i):
            if i == len(word):
                return True

            if not (0<=x<len(board)) or not (0<=y<len(board[0])) \
            or word[i] != board[x][y] or (x,y) in visited:
                return False

            visited.add((x,y))
           
            res=False
            for r,c in directions:
                if dfs(x+r,y+c,i+1):
                    res= True

            visited.remove((x,y))
            return res
        
        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True

        return False
