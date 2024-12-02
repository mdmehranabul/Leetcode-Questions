class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for val in tokens:
            if val =="+":
                b=stack.pop()
                a=stack.pop()
                calc=a+b
                stack.append(calc)

            elif val=="*":
                b=stack.pop()
                a=stack.pop()
                calc=a*b
                stack.append(calc)

            elif val=="-":
                b=stack.pop()
                a=stack.pop()
                calc=a-b
                stack.append(calc)

            elif val=="/":
                b=stack.pop()
                a=stack.pop()
                calc=int(a/b)
                stack.append(calc)

            else: 
                stack.append(int(val))
            
        return stack.pop()
            

# Time Complexity - O(n)
# Space complexity - O(n)