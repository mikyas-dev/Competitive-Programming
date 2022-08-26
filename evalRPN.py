class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isinteger(a):
            try:
                int(a)
                return True
            except ValueError:
                return False
        lis=[]
        for i in range(len(tokens)):
            if isinteger(tokens[i]):
                lis.append(int(tokens[i]))
            elif tokens[i]=="+":
                lis.append(lis.pop()+lis.pop())
            elif tokens[i]=="-":
                x=lis.pop()
                y=lis.pop()
                lis.append(y-x)
            elif tokens[i]=="*":
                lis.append(lis.pop()*lis.pop())
            elif tokens[i]=="/":
                x=lis.pop()
                y=lis.pop()
                lis.append(int(y/x))
        return lis[0]
                
