class Solution:
    def climbStairs(self, n: int) -> int:
        # def recur(i):
        #     if i==n: return 1
        #     if i>n: return 0

        #     return recur(i+1) + recur(i+2)
        
        # return recur(0)

        # cache=[-1]*(n+1)

        # def recur(i,cache):
        #     if i>n: return 0
        #     if cache[i]!=-1:
        #         return cache[i]
            
        #     if i==n: return 1
            

        #     cache[i]=recur(i+1,cache)+recur(i+2,cache)

        #     return cache[i]
        
        # return recur(0,cache)

        if n<=2: return n
        dp=[0]*(n+1)

        dp[1],dp[2]=1,2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]


    




        