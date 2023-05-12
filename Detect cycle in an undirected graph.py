from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
        
        color = [0]*V
        def dfs(node,p):
            if color[node] == 2:
                return False
            if color[node] == 1:
                return True
            
            color[node] = 1
            for neig in adj[node]:
                if neig != p:
                    if dfs(neig,node):
                        return True
                
            color[node] = 2
            return False
        
        for i in range(V):
            if color[i] == 2:
                continue
            if dfs(i,-1):
                return True
        
        return False

