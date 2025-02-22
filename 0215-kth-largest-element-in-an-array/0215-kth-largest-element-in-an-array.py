class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums2=[-n for n in nums]
        heapq.heapify(nums2)

        while k>0:
            val=heapq.heappop(nums2)
            k-=1

        return -val