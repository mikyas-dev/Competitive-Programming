import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(graph, start):
            dist = {node: float('inf') for node in graph}
            dist[start] = 0
            priority_queue = [(0, start)]
            visited = set()
            
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_node in visited:
                    continue
                visited.add(current_node)
                for neighbor, weight in graph[current_node].items():
                    distance = current_distance + weight
                    if distance < dist[neighbor]:
                        dist[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
            return dist
        
        
        
        graph = {i: {} for i in range(1, n+1)}
        for u, v, w in times:
            graph[u][v] = w
        dist = dijkstra(graph, k)
        return max(dist.values()) if max(dist.values()) != float('inf') else -1
