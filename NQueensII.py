def totalNQueens(self, n: int) -> int:
  """
  Read NQueens 1 if you need details. It's the same exact solution except instead of having to keep track of an answer 
  variable we can just initialize a global count variable and add 1 to it whenever r==n.
  """
        count = [0]

        col,posdiag,negdiag = set(),set(),set()

        board = [['.']*n for _ in range(n)]

        def backtrack(r):
            if r ==n:
                count[0] +=1
                return
            for c in range(n):
                if c in col or r+c in posdiag or r-c in negdiag:
                    continue
                
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]='Q'
                backtrack(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]='.'

            return
        backtrack(0)

        return count[0]
