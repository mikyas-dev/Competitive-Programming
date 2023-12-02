class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (start, end), wei in zip(equations, values):
            graph[start][end] = wei
            graph[end][start] = 1/wei

        def dfs(start, end, ans):
            if start == end:
                result.append(ans)
                return True
            visited.add(start)
            
            for nxt, wei in graph[start].items():
                if nxt not in visited:
                    if dfs(nxt, end, ans *wei):
                        return True
            return False
        result = []
        for start, end in queries:
            visited = set()
            if end not in graph or start not in graph:
                result.append(-1)
                continue

            if not dfs(start, end, 1):
                result.append(-1)
        
        return result

                    

        