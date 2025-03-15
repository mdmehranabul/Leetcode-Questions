class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        largest=0

        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                stackind,stackh=stack.pop()
                largest=max(largest,(i-stackind)*stackh)
                start=stackind
            stack.append([start,h])

        for i,h in stack:
            largest=max(largest,(len(heights)-i)*h)
        return largest
        
        