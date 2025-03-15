class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for c in tokens:
            if stack and c=="+":
                b=int(stack.pop())
                a=int(stack.pop())
                calc=a+b
                stack.append(calc)
            elif stack and c=="-":
                b=int(stack.pop())
                a=int(stack.pop())
                calc=a-b
                stack.append(calc)
            elif stack and c=="*":
                b=int(stack.pop())
                a=int(stack.pop())
                calc=a*b
                stack.append(calc)
            elif stack and c=="/":
                b=int(stack.pop())
                a=int(stack.pop())
                calc=a/b
                stack.append(calc)
            else: stack.append(c)
        
        return (int(stack[-1]))
            
            

        