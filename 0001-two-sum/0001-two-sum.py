class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in hashmap:
                return [i,hashmap[diff]]
            else: hashmap[n]=i
        return

# Time Complexity - O(length of the list)
# Space Complexity - O(length of the list)

        