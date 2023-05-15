def solveNQueens(self, n: int) -> List[List[str]]:
  """
  Basically what you want to do is set up the board with .'s for it to be empty and set up column, and diagonal sets to
  store information. The trick is to set up a function that takes the row as an input then in the function you loop over
  the column positions placing a queen at board[row][col] and seeing if that would work as a solution. To do this,
  we need to add change the board from a . to a Q add the change to our sets and then call the backtracking algorithm. 
  After this, we undo all the changes to the set we caused and then move onto the next position in the columns.
  
  Here col is the set that lets us know that we have a Queen in this column, posdiag lets us know that we have a queen
  on the left to right diagonal (northwest to southeast) and negdiag lets us know that we have a queen on the right to left
  diagonal (northeast to southwest).
  """
        col,posdiag,negdiag = set(),set(),set()

        res = []
        board = [['.']*n for _ in range(n)]

        def backtrack(r):
            if r==n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or r+c in posdiag or r-c in negdiag:
                    continue

                #Add a queen at this position and mark the board and sets
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]="Q"
                backtrack(r+1) #backtrack after saying we put a queen at
                #this row

                #Undo our marking so we can continue onto the 
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]='.'
        backtrack(0)
        return res
