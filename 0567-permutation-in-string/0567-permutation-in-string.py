class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2): return False

        hash1=[0]*26
        hash2=[0]*26
        l=0
        for i in range(len(s1)):
            hash1[ord(s1[i])-ord('a')]+=1
            hash2[ord(s2[i])-ord('a')]+=1

        for r in range(len(s1),len(s2)):
            if hash1==hash2: return True

            hash2[ord(s2[r])-ord('a')]+=1
            hash2[ord(s2[l])-ord('a')]-=1
            
            l+=1
        return hash1==hash2

# Time Complexity - O(n) where n is length of s2
# Space Complexity - O(26*2) ~ O(1)

# Time Complexity 