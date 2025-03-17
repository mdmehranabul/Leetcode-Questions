class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,curr=[],[]

        def backtrack(i):
            if i==len(s):
                res.append(curr.copy())
                return
            
            for j in range(i,len(s)):
                if self.palin(s[i:j+1]):
                    curr.append(s[i:j+1])
                    backtrack(j+1)
                    curr.pop()
            
            return res
        backtrack(0)
        return res

    def palin(self,s):
        return s==s[::-1]
        