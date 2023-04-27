class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        if grid[0][0]:
            return -1
        visited = set([(0,0)])
        queue = deque([(0,0,1)])

        def isbound(row,col):
            return (0 <= row < len(grid) and 0 <= col < len(grid))
        
        while queue:
            r,c,d = queue.popleft()
            if r == len(grid) -1 and c == len(grid) - 1:
                return d
            
            for dx,dy in direction:
                newr,newc = r+dx,c+dy
                if isbound(newr,newc) and (newr,newc) not in visited and not grid[newr][newc]:
                    visited.add((newr,newc))
                    queue.append((newr,newc,d+1))

        return -1