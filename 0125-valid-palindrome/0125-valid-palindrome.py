class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:
            while l<r and self.isalpha(s[l])==False:
                l+=1
            while l<r and self.isalpha(s[r])==False:
                r-=1
            if l<r and s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True


    
    def isalpha(self,s):
        return (ord('a') <= ord(s) <= ord('z') or 
            ord('0') <= ord(s) <= ord('9') or
            ord('A') <= ord(s) <= ord('Z'))
        