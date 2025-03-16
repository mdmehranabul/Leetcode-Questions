class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr,res=[],[]
        nums.sort()
        def backtrack(i):
            if i==len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            while i+1>0 and i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1)
        
        backtrack(0)
        return res


        