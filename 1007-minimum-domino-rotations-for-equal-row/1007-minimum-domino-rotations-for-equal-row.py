class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        def check(x):
            cnt_top_swap,cnt_bot_swap=0,0

            for i in range(len(tops)):
                if tops[i]!=x and bottoms[i]!=x:
                    return float('inf')
                
                elif tops[i]!=x: cnt_top_swap+=1
                elif bottoms[i]!=x: cnt_bot_swap+=1
            
            return min(cnt_top_swap,cnt_bot_swap)
        res=min(check(tops[0]),check(bottoms[0])) 
        return res if res!= float('inf') else -1

        