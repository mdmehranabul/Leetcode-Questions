class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0": return "0"

        n=len(num1)+len(num2)
        res=[0]*n

        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):

                mul=int(num1[i])*int(num2[j])
                summ=mul+res[i+j+1]
                res[i+j+1]=summ%10
                res[i+j]+=summ//10
        
        result_str = ''.join(map(str, res)).lstrip('0')
        return result_str

# Time complexity - O(n x m)
# Space complexity - O(n + m)