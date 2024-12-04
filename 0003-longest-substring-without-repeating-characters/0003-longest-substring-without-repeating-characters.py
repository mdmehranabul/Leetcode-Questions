class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res,l=0,0
        hashset=set()

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            res=max(res,r+1-l)
        return res
# Time Complexity - O(n)
# Space Complexity - O(n)