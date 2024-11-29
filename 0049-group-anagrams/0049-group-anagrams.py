class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            count=[0]*26

            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())

# Time Complexity - O(m x n)
# Space Complexity - O(m) where m is the number of strings and n is the length of the longest string.