class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        adj={i:[] for i in range(numCourses)}

        for x,y in prerequisites:
            adj[y].append(x)
        res=[]
        def dfs(crs):
            if crs not in premap:
                premap[crs]=set()
                for nei in adj[crs]:
                    premap[crs]|=dfs(nei)
            premap[crs].add(crs)
            return premap[crs]

        premap={}
        for i in range(numCourses):
            dfs(i)   
        for x,y in queries:
            res.append(x in premap[y])
        return res
        
            
