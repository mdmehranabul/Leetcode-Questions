class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,curset=[],[]

        def dfs(i):
            if i==len(nums):
                return [[]]
            
            curset=dfs(i+1)
            local_res=[]
            for p in curset:
                for j in range(len(p)+1):
                    pcopy=p.copy()
                    pcopy.insert(j,nums[i])
                    local_res.append(pcopy)
                    #print(local_res)
            
            return local_res
        
        res=dfs(0)
        return res

# Time Complexity - O(n x n!)
# Space Complexity - O(n x n!)
