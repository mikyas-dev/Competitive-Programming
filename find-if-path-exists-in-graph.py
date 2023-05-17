class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = {i : set() for i in range(n)}

        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        
        visted = set()
        ans = False
        def dfs(vertex):
            nonlocal ans,visted
            if vertex == destination:
                ans = True
                return
            
            if len(visted)==n:
                return
            
            visted.add(vertex)
            for neighbour in adj[vertex]:
                if neighbour not in visted:
                    dfs(neighbour)
            
        dfs(source)
        return ans