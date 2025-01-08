class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curset,res=[],[]
        candidates.sort()
        def dfs(i,total):
            if total==target:
                res.append(curset.copy())
                return
            
            if i==len(candidates) or total>target:
                return
            
            curset.append(candidates[i])
            dfs(i+1,total+candidates[i])
            curset.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,total)
        dfs(0,0)
        return res

# Time Complexity - O(n*2^n)
# Space Complexity - O(n)
        