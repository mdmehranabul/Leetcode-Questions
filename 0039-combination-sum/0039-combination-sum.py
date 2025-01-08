class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curset,res=[],[]

        def dfs(i,total):
            if i==len(candidates) or total>target:
                return
            
            if total==target:
                res.append(curset.copy())
                return
            #print(curset)
            curset.append(candidates[i])
            dfs(i,total+candidates[i])
            curset.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res
    
# Time Complexity - O(T.2^n)
# Space Complexity - O(T)