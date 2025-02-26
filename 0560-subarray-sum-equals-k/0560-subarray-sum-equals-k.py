class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_hash={0:1}
        curr_sum=0
        res=0


        for n in nums:
            curr_sum+=n
            diff=curr_sum-k
            res+=prefix_hash.get(diff,0)
            prefix_hash[curr_sum]=1+prefix_hash.get(curr_sum,0)

        print(prefix_hash)
        return res
                

        