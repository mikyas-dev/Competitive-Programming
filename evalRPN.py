class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in ('+','-','/','*'):
                stack.append(int(i))
            elif i=='+':
                stack.append(stack.pop()+stack.pop())
            elif i=='-':
                num1,num2=stack.pop(),stack.pop()
                stack.append(num2-num1)
            elif i=='/':
                num1,num2=stack.pop(),stack.pop()
                stack.append(int(num2/num1))
            elif i=='*':
                stack.append(stack.pop()*stack.pop())
        return stack[-1]
