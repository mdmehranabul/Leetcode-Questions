class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L,U=1,max(piles)

        while L<=U:
            mid=L+(U-L)//2
            tot=0
            for p in piles:
                tot+=math.ceil(float(p)/mid)
            
            if tot>h:
                L=mid+1
            else:
                U=mid-1
        return L

#Time Complexity : O(n⋅log(max(piles)))
#Space Complexity : O(1)
        




#Time Complexity : O(n⋅log(max(piles)))
#Space Complexity : O(1)
        