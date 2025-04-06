class Solution:
    def climbStairs(self, n: int) -> int:
        # def dfs(i):
        #     if i>n: return 0
        #     if i==n: return 1

        #     return dfs(i+1)+dfs(i+2)
        # return dfs(0)
        # cache=[-1]*(n+1)
        # def dfs(i,cache):
        #     if i>n: return 0
        #     if i==n: return 1

        #     if cache[i]!=-1: return cache[i]

        #     cache[i]=dfs(i+1,cache)+dfs(i+2,cache)

        #     return cache[i]
        # return dfs(0,cache)

        # if n<=2: return n

        # dp=[0]*(n+1)

        # dp[1],dp[2]=1,2

        # for i in range(3,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        
        # return dp[n]

        if n<=2: return n

        a,b=1,2

        for i in range(n-2):
            a,b=b,a+b
        return b

