class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N=len(colors)
        res=0
        l=0

        for r in range(1,N+k-1):
            if colors[r%N]==colors[(r-1)%N]:
                l=r
            
            if (r+1-l)>k:
                l+=1
            
            if (r+1-l)==k:
                res+=1
        
        return res