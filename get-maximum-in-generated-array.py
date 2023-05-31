class Solution:
    def __init__(self):
        self.memo = dict()
        self.memo[0] = 0
        self.memo[1] = 1
        self.large = 0

    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        for i in range(n+1):
            self.dp(i)
        # print(self.memo)
        return max(self.memo.values())
        
    def dp(self,n):
        if n in self.memo:
            return self.memo[n]
        if n %2==0:
            self.memo[n] = self.dp(n//2)
        else:
            i = int(n/2)
            self.memo[n] = self.dp(i+1)+ self.dp(i)
        return self.memo[n]