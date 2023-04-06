class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        

        adj = {i:set() for i in range(n)}

        for road in roads:
            adj[road[0]].add(road[1])
            adj[road[1]].add(road[0])
        
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                temp = len(adj[i])+len(adj[j])
                if i in adj[j]:
                    temp -= 1
                ans = max(temp,ans)




        
        return ans
