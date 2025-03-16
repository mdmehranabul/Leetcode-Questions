class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        hashset=set()
        maxlen=0
        while r<len(s):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            maxlen=max(maxlen,r+1-l)
            r+=1
        return maxlen
        