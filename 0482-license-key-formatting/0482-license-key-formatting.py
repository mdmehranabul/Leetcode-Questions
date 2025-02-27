class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res=[]
        s=s.upper()
        s=s.replace('-','')
        s=s[::-1]
        print(s)

        for i in range(0,len(s),k):
            res.append(s[i:i+k])
            print(s[i:i+k])
        
        return ("-".join(res)[::-1])