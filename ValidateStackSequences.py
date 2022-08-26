class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        pu=po=0
        while pu<len(pushed):
            stack.append(pushed[pu])
            while stack and stack[-1]==popped[po]:
                stack.pop()
                po+=1
            pu+=1
        return 0==len(stack)
