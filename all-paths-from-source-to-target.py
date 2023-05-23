class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node,arr):
            if node == len(graph)-1:
                ans.append(arr[:])
                return 
            

            for ch in graph[node]:
                arr.append(ch)
                dfs(ch,arr)
                arr.pop()
        
        ans = []
        dfs(0,[0])
        return ans