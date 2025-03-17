class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        subset,curr=[],[]
        hashmap={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtrack(i):
            if i==len(digits):
                subset.append("".join(curr))
                return
            
            for c in hashmap[digits[i]]:
                curr.append(c)
                backtrack(i+1)
                curr.pop()
            
            return subset
        
        if digits: backtrack(0)

        return subset
