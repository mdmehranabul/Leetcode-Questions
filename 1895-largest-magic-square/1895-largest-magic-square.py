class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Precompute prefix sums for rows and columns
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * (m + 1) for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
                col_prefix[j][i + 1] = col_prefix[j][i] + grid[i][j]

        # Helper to calculate sum of a row
        def get_row_sum(row, start, end):
            return row_prefix[row][end] - row_prefix[row][start]
        
        # Helper to calculate sum of a column
        def get_col_sum(col, start, end):
            return col_prefix[col][end] - col_prefix[col][start]

        # Check if a k x k subgrid is a magic square
        def is_magic_square(r, c, k):
            target = get_row_sum(r, c, c + k)
            
            # Check row sums
            for i in range(r, r + k):
                if get_row_sum(i, c, c + k) != target:
                    return False
            
            # Check column sums
            for j in range(c, c + k):
                if get_col_sum(j, r, r + k) != target:
                    return False
            
            # Check diagonals
            diag1 = sum(grid[r + i][c + i] for i in range(k))
            diag2 = sum(grid[r + i][c + k - i - 1] for i in range(k))
            if diag1 != target or diag2 != target:
                return False
            
            return True

        # Iterate over all possible subgrids
        max_size = 1  # Every 1x1 grid is trivially a magic square
        for r in range(m):
            for c in range(n):
                for k in range(2, min(m - r, n - c) + 1):
                    if is_magic_square(r, c, k):
                        max_size = max(max_size, k)

        return max_size
