class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque([(0, 1, 0)])
        visited = set()
        while queue:
            position, speed, steps = queue.popleft()
            if position == target:
                return steps
            if (position, speed) in visited:
                continue
            visited.add((position, speed))
            queue.append((position + speed, speed * 2, steps + 1))
            queue.append((position, -1 if speed > 0 else 1, steps + 1))