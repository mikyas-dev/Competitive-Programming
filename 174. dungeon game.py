class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0
        
        m, n = len(dungeon), len(dungeon[0])
        
        # Create a 2D array to store the minimum health required at each cell
        dp = [[0] * n for _ in range(m)]
        
        # Start from the bottom-right cell
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])  # Minimum health needed to survive
        
        # Fill the last column
        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(dp[i + 1][-1] - dungeon[i][-1], 1)
        
        # Fill the last row
        for j in range(n - 2, -1, -1):
            dp[-1][j] = max(dp[-1][j + 1] - dungeon[-1][j], 1)
        
        # Fill the remaining cells from bottom to top, right to left
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_required_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(min_required_on_exit - dungeon[i][j], 1)
        
        return dp[0][0]  