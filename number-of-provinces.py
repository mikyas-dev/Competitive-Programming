class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:graph[i+1].append(j+1)
        
        def dfs(key):
            if key in visited:
                return
            
            visited.add(key)

            for val in graph[key]:
                dfs(val)
        
        visited = set()
        # for key
        ans = 0
        for key,val in graph.items():
            if key not in visited:
                ans += 1
                dfs(key)
        return ans