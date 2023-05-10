class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        mygraph = defaultdict(set)
        indegree = [0]*len(graph)

        for i in range(len(graph)):
            for val in graph[i]:
                mygraph[val].add(i)
            indegree[i]=len(graph[i])
       
        queue = deque()
        for i,v in enumerate(indegree):
            if v == 0:
                queue.append(i)
        ans = []
        while queue:
            node = queue.popleft()
            for neig in mygraph[node]:
                indegree[neig]-=1
                if indegree[neig] == 0:
                    queue.append(neig)

        for i,v in enumerate(indegree):
            if v == 0:
                ans.append(i)
        
        return ans