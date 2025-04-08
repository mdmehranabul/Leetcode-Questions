class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # def dfs(i):
        #     if i>=len(cost):
        #         return 0
        #     return cost[i]+min(dfs(i+1),dfs(i+2))
        
        # return min(dfs(0),dfs(1))
        n=len(cost)
        cache=[-1]*(n+1)

        def dfs(i):
            if i>=len(cost):
                return 0
            if cache[i]!=-1: return cache[i]
            cache[i]=cost[i]+min(dfs(i+1),dfs(i+2))
            return cache[i]
            
        return min(dfs(0),dfs(1))


            

            
        