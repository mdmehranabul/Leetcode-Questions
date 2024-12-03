class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        L=1
        U=max(piles)
        tot=0
        while U>=L:
            mid=L+(U-L)//2
            tot=0
            for p in piles:
                tot+=math.ceil(float(p)/mid)
            if tot<=h:
                U=mid-1
            else:
                L=mid+1
        return L

#Time Complexity : O(n⋅log(max(piles)))
#Space Complexity : O(1)
        