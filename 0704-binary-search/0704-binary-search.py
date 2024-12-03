class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,U=0,len(nums)-1
        #M=int((U+L)/2)

        while L<=U:
            M=L+(U-L)//2
            if (nums[M]==target):
                return M
            elif nums[M]<target:
                L=M+1
            else:
                U=M-1
        return -1

#Time Complexity - O(log n)
#Space Complexity - O(n)
        