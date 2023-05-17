class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = {i+1:i+1 for i in range(len(edges))}
        ans = []
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x,y):
            parent_x = find(x)
            parent_y = find(y)
            root[parent_x] = parent_y
            if parent_x == parent_y:
                return True
            

        
        for a,b in edges:
            
            if union(a,b):
                ans = [a,b]
        
        return ans