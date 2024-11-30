class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        pre,post=1,1

        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            res[j]*=post
            post*=nums[j]
            print(post)
        return res

# Time Complexity - O(n)
# Space Complexity - O(1)
        