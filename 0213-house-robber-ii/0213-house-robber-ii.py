class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums)==1: return nums[0]

        # def dfs(i,arr):
        #     if i>=len(arr):
        #         return 0
            
        #     return max(arr[i]+dfs(i+2,arr),dfs(i+1,arr))
        # return max(dfs(0,nums[1:]),dfs(0,nums[:-1]))

        # if len(nums)==1: return nums[0]
        # n=len(nums)
        # #cache=[-1]*(n+1)
        # def dfs(i,arr,cache):
        #     if i>=len(arr):
        #         return 0
        #     if cache[i]!=-1: return cache[i]
        #     cache[i]= max(arr[i]+dfs(i+2,arr,cache),dfs(i+1,arr,cache))
        #     return cache[i]
        # return max(dfs(0,nums[1:],[-1]*(n+1)),dfs(0,nums[:-1],[-1]*(n+1)))
        
        def dfs(nums):
            if len(nums)==0: return 0
            if len(nums)==1: return nums[0]

            rob1,rob2=nums[0],max(nums[0],nums[1])

            for i in range(2,len(nums)):
                rob1,rob2=rob2,max(rob2,rob1+nums[i])
            
            return rob2
        
        return max(dfs(nums[1:]),dfs(nums[:-1]))
