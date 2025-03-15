class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length=0
        longest=0
        hashset=set(nums)
        for n in hashset:
            if n-1 not in hashset:
                length=1
                while n+length in hashset:
                    length+=1
                longest=max(longest,length)
        
        return longest

        