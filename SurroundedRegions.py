class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        The question asks us for the number of surrounded regions but what is easier to do is to first capture the unsurrounded regions (which will be those
        that are connected to the edge of the board) and mark them with a temporary variable, then capture everything else, then uncapture the unsurrounded
        elements. This makes everything rather simple. So loop through the board and run dfs on the edges of the board that are "O"'s. Your dfs algorithm 
        will have a base case of checking that the pointers are valid and the value at that point is indeed an O and then will change the value to a temporary
        value and run dfs on all cardinal neighbors. So we loop on the board and run dfs on the edges that have O's to see what's happening. Then loop over 
        the board again to see which values weren't captured to now change them to X's and then change our temporary values back to O's. This solves 
        the problem in a relatively simple way.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r,c):
            if r < 0 or c <0 or r==rows or c == cols or board[r][c] != "O":
                return 
            
            board[r][c] = "T"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        #find the unsurrounded regions (the ones connected to the border) (O->T)
        
        for r in range(rows):
            for c in range(cols):
                if ((r in [0,rows-1] or c in [0,cols-1]) and board[r][c]=="O"):
                    dfs(r,c)
                    
        #capture the surrounded regions (O->X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c] = "X"
                    
        #Uncapture unsurrounded regions (T->O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c] = "O"
