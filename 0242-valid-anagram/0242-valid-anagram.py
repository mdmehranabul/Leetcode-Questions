class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        hash_t={}
        hash_s={}

        for i in range(len(s)):
            hash_s[s[i]]=1+hash_s.get(s[i],0)
            hash_t[t[i]]=1+hash_t.get(t[i],0)
        

        for c in s:
            if hash_s[c]!=hash_t.get(c,0):
                return False
        return True
        