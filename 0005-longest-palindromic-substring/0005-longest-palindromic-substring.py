class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=0
        res=""

        for i in range(len(s)):
            l,r=i,i

            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r+1-l) > length:
                    length=r+1-l
                    res=s[l:r+1]
                l-=1
                r+=1

        for i in range(len(s)):
            l,r=i,i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r+1-l) > length:
                    length=r+1-l
                    res=s[l:r+1]
                l-=1
                r+=1
        return res

# Time Complexity - O(n^2)
# Space Complexity - O(n)