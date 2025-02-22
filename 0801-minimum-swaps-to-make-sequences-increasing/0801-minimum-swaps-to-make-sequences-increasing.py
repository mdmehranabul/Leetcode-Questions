class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # n=len(nums1)

        # swap=[float("inf")]*n
        # noswap=[float("inf")]*n

        # swap[0]=1
        # noswap[0]=0

        # for i in range(1,n):
        #     if nums1[i]> nums1[i-1] and nums2[i]>nums2[i-1]:
        #         noswap[i]=noswap[i-1]
        #         swap[i]=swap[i-1] + 1
        #     if nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]:
        #         noswap[i]=min(noswap[i],swap[i-1])
        #         swap[i]=min(swap[i],noswap[i-1]+1)
        # print(noswap)
        # print(swap)
        # return min(noswap[-1],swap[-1])

        n=len(nums1)

        prev_swap=1
        prev_noswap=0

        for i in range(1,n):
            swap,noswap=float("inf"),float("inf")
            if nums1[i]> nums1[i-1] and nums2[i]>nums2[i-1]:
                noswap=prev_noswap
                swap=prev_swap + 1
            if nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]:
                noswap=min(noswap,prev_swap)
                swap=min(swap,prev_noswap+1)

            prev_swap,prev_noswap=swap,noswap
        return min(swap,noswap)



        