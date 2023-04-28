class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, queue, visited = len(mat), len(mat[0]), deque(), set()
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0: 
                    queue.append((r, c))
                    visited.add((r, c))
                else:
                    mat[r][c] = -1
        while queue:
            r, c = queue.popleft()
            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        return mat