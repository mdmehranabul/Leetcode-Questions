class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # def dfs(i):
        #     if i>=len(cost):
        #         return 0
        #     return cost[i]+min(dfs(i+1),dfs(i+2))
        
        # return min(dfs(0),dfs(1))
        # n=len(cost)
        # cache=[-1]*(n+1)

        # def dfs(i):
        #     if i>=len(cost):
        #         return 0
        #     if cache[i]!=-1: return cache[i]
        #     cache[i]=cost[i]+min(dfs(i+1),dfs(i+2))
        #     return cache[i]
            
        # return min(dfs(0),dfs(1))

        # dp=[0]*(n+2)

        # for i in range(len(cost)-1,-1,-1):
        #     dp[i]=cost[i]+min(dp[i+1],dp[i+2])
        # return min(dp[0],dp[1])

        for i in range(len(cost)-3,-1,-1):
            cost[i]=cost[i]+min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])


            

            
        