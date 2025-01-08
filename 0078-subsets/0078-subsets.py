class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curset,res=[],[]

        def dfs(i):

            if i==len(nums):
                res.append(curset.copy())
                return
            curset.append(nums[i])
            dfs(i+1)
            curset.pop()
            dfs(i+1)
        dfs(0)
        return res
    
# Time complexity - O(n*2^n)
# Space complexity - O(n)
        