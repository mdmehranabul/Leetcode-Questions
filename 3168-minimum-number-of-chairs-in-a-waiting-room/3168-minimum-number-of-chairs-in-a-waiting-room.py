class Solution:
    def minimumChairs(self, s: str) -> int:
        res=0
        enter=0

        for event in s:
            if event=="E":
                enter+=1
            else:
                enter-=1
            res=max(res,enter)
        return (res)
        