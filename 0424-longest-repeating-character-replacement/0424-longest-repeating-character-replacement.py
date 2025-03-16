class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        longest=0
        hashmap=defaultdict(int)

        for r in range(len(s)):
            hashmap[s[r]]+=1
            while (r+1-l)-max(hashmap.values())>k:
                hashmap[s[l]]-=1
                l+=1
            longest=max(longest,r+1-l)
        return longest

        