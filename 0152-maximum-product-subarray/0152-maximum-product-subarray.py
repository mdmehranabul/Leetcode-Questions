class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max,curr_min=1,1
        res=max(nums)

        for n in nums:

            curr_max,curr_min=max(n*curr_max,n*curr_min,n),min(n*curr_max,n*curr_min,n)
            res=max(res,curr_max)
        return res
        