class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)

        left=0
        while (left+1)<n and arr[left+1]>=arr[left]:
            left+=1
        
        if left==n-1: return 0

        #print(left)
        right=n-1
        while right>0 and arr[right]>=arr[right-1]:
            right-=1
        
        res=min(right,n-left-1)
        print(res)

        left2=0

        while left2<=left and right<n:
            if arr[left2]<=arr[right] :
                res=min(res,right-left2-1)
                left2+=1
            else:
                right+=1
        return res