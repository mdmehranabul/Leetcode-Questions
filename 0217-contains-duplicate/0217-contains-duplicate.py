class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash=set()

        for n in nums:
            if n in hash: return True
            else: hash.add(n)
        return False
# Time Complexity : O(n)
# Space Complexity : O(n) where n is the length of nums