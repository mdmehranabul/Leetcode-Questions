class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum,res=0,0
        min_sum,max_sum=0,0

        for n in nums:
            curr_sum+=n
            print(curr_sum)
            res=max(res,abs(curr_sum-min_sum),abs(curr_sum-max_sum))
            min_sum=min(min_sum,curr_sum)
            max_sum=max(max_sum,curr_sum)
        return res