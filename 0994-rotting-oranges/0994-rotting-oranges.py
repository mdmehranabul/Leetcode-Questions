class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        visited=set()
        rows,cols=len(grid),len(grid[0])
        time,fresh=0,0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    visited.add((r,c))
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1


        
        def update_grid(r,c):
            if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c]!=0:
                q.append((r,c))
                visited.add((r,c))
                grid[r][c]=2
                return True
            return False
        

        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                if grid[r][c]==2:
                    if update_grid(r+1,c): fresh-=1
                    if update_grid(r-1,c): fresh-=1
                    if update_grid(r,c+1): fresh-=1
                    if update_grid(r,c-1): fresh-=1

            time+=1
        return time if fresh==0 else -1
        