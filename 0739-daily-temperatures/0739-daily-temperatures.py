class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                temp,ind=stack.pop()
                res[ind]=i-ind
            
            stack.append([t,i])
        return res

#Time Complexity - O(n)
#Space Complexity - O(n)