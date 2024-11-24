class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2=0,0

        # [1,2,3,1]

        for n in nums:
            temp=max(rob1+n,rob2)
            #print(temp)
            rob1=rob2
            #print("rob2:",rob2)
            rob2=temp
        return rob2
        