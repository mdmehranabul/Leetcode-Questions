class Solution:
    def rob(self, nums: List[int]) -> int:

        # def dfs(i):
        #     if i>=len(nums): return 0

        #     return max(nums[i]+dfs(i+2),dfs(i+1))
        # return dfs(0)
        
        # cache=[-1]*(len(nums))
        # def dfs(i):
        #     if i>=len(nums): return 0

        #     if cache[i]!=-1: return cache[i]
        #     cache[i]=max(nums[i]+dfs(i+2),dfs(i+1))

        #     return cache[i]
        
        # return dfs(0)


        # dp=[0]*(len(nums)+2)
        # print(dp)
        # for i in range(len(nums)-1,-1,-1):
        #     dp[i]=max(nums[i]+dp[i+2],dp[i+1])
        # print(dp)

        # return max(dp[0],dp[1])

        if len(nums)==1: return nums[0]
        rob1,rob2=nums[0],max(nums[0],nums[1])

        for i in range(2,len(nums)):
            rob1,rob2=rob2,max(rob2,nums[i]+rob1)
        print(rob1,rob2)
        return (rob2)








