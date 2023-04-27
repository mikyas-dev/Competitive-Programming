class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set([0])
        queue = deque([0])

        while queue:
            idx = queue.popleft()

            for val in rooms[idx]:
                if val not in visited:
                    visited.add(val)
                    queue.append(val)
        
        return n == len(visited)