class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        hashset,window={},{}
        for c in t:
            hashset[c]=1+hashset.get(c,0)
        
        l=0
        res=[-1,-1]
        reslen=float("infinity")

        have,need=0,len(hashset)

        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)

            if s[r] in hashset and window[s[r]]==hashset[s[r]]:
                have+=1
        
            while have ==need:
                if r+1-l <reslen:
                    res=[l,r]
                    reslen=r+1-l

                window[s[l]]-=1
                #print(res)
                if s[l] in hashset and window[s[l]]<hashset[s[l]]:
                    have-=1
                l+=1
        l,r=res

        return s[l:r+1] if reslen !=float("infinity") else ""

# Time Complexity - O(n) where n is the length of the string s
# Space Complexity - O(m) where m is the no of unique characters in s