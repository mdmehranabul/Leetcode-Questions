class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        pac,atl=set(),set()
        ROWS,COLS=len(heights),len(heights[0])

        def dfs(r,c,visited,prevheight):

            if r in range(ROWS) and c in range(COLS) and (r,c) not in visited and heights[r][c]>=prevheight:
                visited.add((r,c))
                dfs(r+1,c,visited,heights[r][c])
                dfs(r-1,c,visited,heights[r][c])
                dfs(r,c+1,visited,heights[r][c])
                dfs(r,c-1,visited,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])


        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
        