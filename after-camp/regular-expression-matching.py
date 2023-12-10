class Solution:

    def func(self, i,j) :

        if self.dp[i][j] != -1 :
            return self.dp[i][j]

        if i==len(self.s) and j==len(self.p) :
            return True 
        if i>=len(self.s):
            
            while(j<len(self.p)-1) :
                if self.p[j+1] == "*" :
                    j += 2 
                else :
                    return False 
            if j >= len(self.p) : 
                return True 
            return False
            
        if j>=len(self.p) :
            return False
        
        a = False
        b = False
        
        if j<len(self.p)-1 :
            if self.p[j+1] == "*" :
                if self.s[i] == self.p[j] :
                    a = self.func(i+1,j)
                elif self.p[j] == "." :
                    a = self.func(i+1,j)
                b = self.func(i , j+2) 
            elif self.p[j] == "." :
                a = self.func(i+1 , j+1) 
            else :
                if self.p[j] == self.s[i] :
                    a = self.func(i+1,j+1)
                else :
                    return False
        elif self.p[j] == "." :
            a = self.func(i+1 , j+1) 
        else :
            if self.p[j] == self.s[i] :
                a = self.func(i+1,j+1)
            else :
                return False 
        self.dp[i][j] = a or b
        return a or b
        
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s 
        self.p = p 
        self.dp = [[-1 for i in range(len(p)+1)] for j in range(len(s)+1)]
        return self.func(0,0)
        