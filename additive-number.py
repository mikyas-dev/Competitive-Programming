class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        s = num
        def dfs(first, second, idx):
            if idx >= len(s):
                return True
            
            for k in range(idx, len(s)):
                curNum = s[idx: k+1]
                
                if (idx != k) and curNum[0] == "0":
                    return False
                
                if (int(first) + int(second) == int(curNum)) and dfs(second, curNum, k+1):
                    return True
            
            return False
        
        
        for i in range(len(s)-2):
            firstNum = s[:i+1]
            if i!= 0 and firstNum[0] == "0":
                return False
            
            for j in range(i+1, len(s)-1):
                secondNum = s[i+1:j+1]
                if (i+1 != j) and secondNum[0] == "0":
                    break
                
                if dfs(firstNum, secondNum, j+1):
                    return True
        
        return False