class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions= [(0,1),(1,0),(-1,0),(0,-1)]
        m = len(grid1[0])
        n = len(grid1)

        def isBounded(row,col):
            return 0 <= row < n and 0 <= col < m
        
        def dfs (row , col , island):
            visited[row][col] = True
            island.append((row,col))

            for dx,dy in directions:
                newRow , newCol = row +dx , col + dy

                if isBounded(newRow , newCol) and grid2[newRow][newCol] ==1 and not visited[newRow][newCol]:
                    dfs( newRow , newCol , island)
            
            return island
        

        def checker(island):

            for row , col in island:
                if not grid1[row][col]:
                    return False

            return True
        

        visited = [[False for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid2[i][j]:
                    island = dfs(i,j,[])
                    if checker(island):
                        ans += 1
        
        return ans


