class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        u , v = edges[0]
        u1, u2 = edges[1]

        if u == u1 or u == u2:
            return u
        return v

            
                
