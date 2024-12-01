class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        max_area=0
        L,R=0, len(height)-1
        
        while L<R:
            
            area=(R-L)*min(height[L],height[R])
            max_area=max(max_area,area)
            
            if height[L]<=height[R]:
                L+=1
            else:
                R-=1
        return max_area

# Time Complexity - O(n)
# Space Complexity - O(1)