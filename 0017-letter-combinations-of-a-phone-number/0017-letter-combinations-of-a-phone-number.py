class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res,curset=[],[]
        mapping={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def dfs(i):
            if i==len(digits):
                res.append("".join(curset.copy()))
                return
            
            for c in mapping[digits[i]]:
                curset.append(c)
                dfs(i+1)
                curset.pop()
            
        if digits:
            dfs(0)
            return res
        else:
            return []

# Time Complexity - O(n x 4^n)
# Space Complexity - O(n)