class Solution:
    def rob(self, nums: List[int]) -> int:

        # def dfs(i):
        #     if i>=len(nums): return 0

        #     return max(nums[i]+dfs(i+2),dfs(i+1))
        # return dfs(0)

# Time Complexity - O(2^n)
# Space Complexity - O(n)

        # cache=[-1]*(len(nums)+1)

        # def dfs(i):
        #     if i>=len(nums): return 0
        #     if cache[i]!=-1: return cache[i]

        #     cache[i]=max(nums[i]+ dfs(i+2),dfs(i+1))
        #     return cache[i]
        
        # return dfs(0)

# Time Complexity - O(n)
# Space Complexity - O(n)
        # if len(nums)==1: return nums[0]
        # dp=[0]* (len(nums))
        # dp[0],dp[1]=nums[0],max(nums[0],nums[1])

        # for i in range(2,len(nums)):
        #     dp[i]=max(nums[i]+ dp[i-2],dp[i-1])
        
        # return dp[-1]
# Time Complexity - O(n)
# Space Complexity - O(n)
        if len(nums)==1: return nums[0]
        rob1,rob2=nums[0],max(nums[0],nums[1])

        for i in range(2,len(nums)):
            rob1,rob2=rob2,max(nums[i]+rob1,rob2)
        
        return rob2

# Time Complexity - O(n)
# Space Complexity - O(1)

        