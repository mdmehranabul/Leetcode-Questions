class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        curset=[["."] * n for i in range(n)]
        res=[]
        col=set()
        posdiag=set()
        negdiag=set()

        def dfs(r):
            if r==n:
                
                res.append(["".join(row) for row in curset])
                return
            
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                
                curset[r][c]="Q"
                col.add(c)
                negdiag.add(r-c)
                posdiag.add(r+c)

                dfs(r+1)
                curset[r][c]="."
                col.remove(c)
                negdiag.remove(r-c)
                posdiag.remove(r+c)
                #print(curset)
        dfs(0)
        return res

            
# Time Complexity - O(n!)
# Space Complexity - O(n^2)