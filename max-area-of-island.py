class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs( row, col):
            nonlocal count
            
            count += 1
            print(count,row,col)
            visited[row][col] = True
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and grid[new_row][new_col]  and not visited[new_row][new_col]:
                    dfs( new_row, new_col)

        ans = 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = 0
                if not visited[i][j] and grid[i][j]:
                    dfs(i,j)
                    ans = max(ans, count)
                
        return ans