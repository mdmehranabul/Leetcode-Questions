class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,curset=[],[]

        def dfs(i):
            if i ==len(nums):
                res.append(curset.copy())
                return
            curset.append(nums[i])
            dfs(i+1)
            curset.pop()

            while i+1 <len(nums) and nums[i]==nums[i+1]:
                i+=1
            
            dfs(i+1)
        
        dfs(0)
        return res

# Time Complexity - O(n*2^n)     
# Space Complexity - O(n)     