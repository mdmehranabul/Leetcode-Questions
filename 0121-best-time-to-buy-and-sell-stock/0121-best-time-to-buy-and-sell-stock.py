class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        prof,maxprof=0,0
        while r<len(prices):
            prof=prices[r]-prices[l]

            if prof>0:
                maxprof=max(maxprof,prof)
            else:
                l=r
            r+=1
        return maxprof
            


        