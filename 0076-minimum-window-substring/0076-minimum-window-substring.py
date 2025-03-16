class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        hashmap={}
        window={}

        for c in t:
            hashmap[c]=1+hashmap.get(c,0)
        reslen=float("inf")
        have,need=0,len(hashmap)
        res=[-1,-1]
        reslen=float("inf")
        l=0

        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)

            if s[r] in hashmap and window[s[r]]==hashmap[s[r]]:
                have+=1
            
            while have==need:
                if (r+1-l) < reslen:
                    res=[l,r]
                    reslen=r+1-l
                
                window[s[l]]-=1

                if s[l] in hashmap and window[s[l]]<hashmap[s[l]]:
                    have-=1
                l+=1
        l,r=res

        return s[l:r+1] if reslen != float("inf") else ""