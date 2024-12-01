class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R=0,len(numbers)-1

        while L<R:
            if numbers[L]+numbers[R]==target:
                return [L+1,R+1]
            elif numbers[L]+numbers[R]>target:
                R-=1
            else:
                L+=1
        return 

#Time Complexity - O(n)
#Space Complexity - O(1)