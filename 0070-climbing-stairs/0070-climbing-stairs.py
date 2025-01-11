class Solution:
    def climbStairs(self, n: int) -> int:

        # def dfs(i):
        #     if i==n: return 1
        #     if i>n: return 0
        #     return dfs(i+1) + dfs(i+2)
        # return dfs(0)
         # Time Complexity - O(2^n)
         # Space Complexity - O(n)
        # cache=[-1]*(n+1)

        # def dfs(i,cache):
        #     if i==n: return 1
            
        #     if i>n: return 0

        #     if cache[i]!=-1: return cache[i]

        #     cache[i]=dfs(i+1,cache)+dfs(i+2,cache)

        #     return cache[i]
        # return dfs(0,cache)

         # Time Complexity - O(n)
         # Space Complexity - O(n)

        # if n<=2: return n
        # dp=[0]*(n+1)
        # dp[1],dp[2]=1,2
        # for i in range(3,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]

         # Time Complexity - O(n)
         # Space Complexity - O(n)


        one,two=1,1

        for i in range(n-1):
            one,two=one+two,one
        return one
         # Time Complexity - O(n)
         # Space Complexity - O(1)
