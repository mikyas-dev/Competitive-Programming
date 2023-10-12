class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and stack[-1][0] ==char:
                stack[-1][1] += 1
            else:
                stack.append([char,1])
            
            flag = stack[-1][1] == k
            if flag:
                stack.pop()
        
        return "".join(char*val for char,val in stack)

        
