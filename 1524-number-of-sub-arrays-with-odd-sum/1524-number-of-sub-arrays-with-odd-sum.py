class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum,odd_cnt,even_cnt,res=0,0,0,0

        for n in arr:
            prefix_sum+=n

            if prefix_sum%2:
                res=res+1+even_cnt
                odd_cnt+=1

            else:
                res=res+odd_cnt
                even_cnt+=1
        return res%(10**9+7)

        