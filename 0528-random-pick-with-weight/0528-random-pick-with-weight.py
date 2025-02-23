class Solution:

    def __init__(self, w: List[int]):
        cum_sum=0
        self.cum_arr=[]

        for weight in w:
            cum_sum+=weight
            self.cum_arr.append(cum_sum)
            
        

    def pickIndex(self) -> int:
        target=random.randint(1,self.cum_arr[-1])
        print(target)
        l,r=0,len(self.cum_arr)-1
        while l<r:
            mid=l+(r-l)//2
            if self.cum_arr[mid]<target:
                l=mid+1
            else:
                r=mid
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()