class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        while queue:
            x, y, step = queue.popleft()
            if (x != entrance[0] or y != entrance[1]) and (x == 0 or x == m - 1 or y == 0 or y == n - 1):
                return step
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    queue.append((nx, ny, step + 1))
                    visited.add((nx, ny))
        return -1
        