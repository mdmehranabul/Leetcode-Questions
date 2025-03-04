class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        # def backtrack(i,tot):
        #     if tot==n: return True
        #     if tot>n or 3**i >n: return False

        #     return backtrack(i+1,tot+3**i) or backtrack(i+1,tot)
        
        # return backtrack(0,0)

        while n>0:
            if n%3==2:
                return False
            n=n//3
        return True
        