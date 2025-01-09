class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,curset=[],[]

        def dfs(i):

            if i==len(s):
                res.append(curset.copy())
            
            for j in range(i,len(s)):
                if self.ispalindrome(s[i:j+1]):
                    curset.append(s[i:j+1])
                    dfs(j+1)
                    curset.pop()
                
        
        dfs(0)
        return res

    def ispalindrome(self,s):
        if s==s[::-1] : return True
        else: return False

# Time Complexity - O(n * 2^n)
# Space Complexity - O(n)