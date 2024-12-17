class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # def removechar(str):
        #     stack=[]

        #     for s in str:
        #         if s =="#":
        #             if stack:
        #                 stack.pop()
        #         else:
        #             stack.append(s)
        #     return stack

        # return removechar(s)==removechar(t)

# Time Complexity - O(m+n)
# Space Complexity - O(m+n)

        i,j=len(s)-1,len(t)-1
        
        while i>=0 or j>=0:
            print(i)
            skip_s=0
            while i>=0 and (s[i]=="#" or skip_s>0):
                if s[i]=="#":
                    skip_s+=1
                else:
                    skip_s-=1
                i-=1
                
            
            skip_t=0
            while j>=0 and (t[j]=="#" or skip_t>0):
                if t[j]=="#":
                    skip_t+=1
                else:
                    skip_t-=1
                j-=1

            if i>=0 and j>=0 and s[i]!=t[j]: return False
            if (i>=0) != (j>=0): return False
            #print(s[i],t[j])
            i-=1
            j-=1
        return True

# Time Complexity - O(m+n)
# Space Complexity - O(1)