class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        prof=0
        maxprof=0

        while r<len(prices):
            prof=prices[r]-prices[l]
            
            #print(prof)
            if prof>0:
                maxprof=max(prof,maxprof)
            else:
                l=r
            r+=1
        return maxprof

#Time Complexity - O(n)
#Space Complexity - O(1)
        