class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS,COLS=len(board),len(board[0])
        def dfs(r,c):
            if r in range(ROWS) and c in range(COLS) and board[r][c]=="O":
                board[r][c]="T"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0,ROWS-1] or c in [0,COLS-1]:
                    dfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="T":
                    board[r][c]="O"