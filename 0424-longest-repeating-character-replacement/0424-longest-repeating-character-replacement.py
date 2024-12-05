class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        longest=0
        hashset={}

        for r in range(len(s)):
            hashset[s[r]]=1+hashset.get(s[r],0)
            while (r+1-l)-max(hashset.values())>k:
                hashset[s[l]]-=1
                l+=1
            longest=max(longest,r+1-l)
        return longest
# Time Complexity - O(26*n)
# Space Complexity - O(26)