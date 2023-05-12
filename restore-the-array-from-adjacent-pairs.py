class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ans =[]
        graph = defaultdict(list)
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        strt = 0
        for key in graph:
            if len(graph[key]) == 1:
                strt = key
                break
        visited = set()

        def dfs(node):
            ans.append(node)
            visited.add(node)

            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr)
        
        dfs(strt)
        return ans