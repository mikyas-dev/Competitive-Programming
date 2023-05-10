class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        queue = deque()
        for i,v in enumerate(indegree):
            if v == 0:
                queue.append(i)
        ans = 0
        while queue:
            node = queue.popleft()
            ans+=1
            for neig in graph[node]:
                indegree[neig]-=1
                if indegree[neig] == 0:
                    queue.append(neig)
        
        return True if ans==numCourses else False