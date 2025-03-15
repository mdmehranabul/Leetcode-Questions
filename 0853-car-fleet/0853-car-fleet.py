class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=[]
        for p,s in zip(position,speed):
            fleet.append((p,s))
        #print(fleet)

        fleet.sort(reverse=True)
        stack=[]

        for p,s in fleet:
            stack.append((target-p)/s)
            while len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)

# Time complexity - O(nlogn)
# Space complexity - O(n)