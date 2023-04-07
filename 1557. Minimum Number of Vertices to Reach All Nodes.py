class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = set()
        for edge in edges:
            adj.add(edge[1])
        
        ans = []
        
        for i in range(n):
            if i not in adj:
                ans.append(i)

        return ans
