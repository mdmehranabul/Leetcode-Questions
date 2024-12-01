class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        L,R=0,len(height)-1
        leftmax,rightmax=height[L],height[R]

        while L<R:
            if leftmax<rightmax:
                L+=1
                leftmax=max(height[L],leftmax)
                res+=leftmax-height[L]
            else:
                R-=1
                rightmax=max(height[R],rightmax)
                res+=rightmax-height[R]
        return res
# Time Complexity - O(n)
# Space Complexity - O(1)