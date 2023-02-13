class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                res=[]
                while stack[-1]!='(':
                    res.append(stack.pop())
                stack.pop()
                stack+=res
        return ''.join(stack)

            
