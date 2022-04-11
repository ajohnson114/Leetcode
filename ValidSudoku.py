class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      """
      Create sets to hold all the numbers in each column (means 9 row sets and 9 column sets). Furthermore we are given a 9 x 9 grid that we are going to
      subdivide into 9 3x3 matrices indexed by 0,1,2. These 0, 1, and 2 indices are mapped to indices (0,1,2), (3,4,5), and (6,7,8) for both 
      columns and rows. We can create this mapping manually by doing floor division where we only keep the integer part of the division. For instance,
      2//3 = 0 which creates the aforementioned mapping. We then identify each matrix by the row and column index mapping technique we just described
      (for instance row 3 and column 4 is in the (1,1) matrix. Having clarified this the rest of the problem is rather simple. Find all the numbers
      if they're already in the hashmaps for their particular row or column it's not a valid sudoku and we should return False, otherwise we add it to
      our hashmaps. If we look at all the numbers and never return False we return True. QED
      
      """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # (row/3,col/3) truncated division
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                    
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or 
                board[i][j] in squares[(i//3,j//3)]):
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
                
        return True
