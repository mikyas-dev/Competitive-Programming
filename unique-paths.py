class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]














        # @cache
        # def dp(row,col):
        #     if (row,col) == (m-1,n-1):
        #         return 1
            
        #     path = 0
        #     if row+1<m:
        #         path += dp(row+1,col)
        #     if col+1<n:
        #         path += dp(row,col+1)
            
        #     return path
        
        # return dp(0,0)