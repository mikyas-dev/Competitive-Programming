class ThroneInheritance:
    

    def __init__(self, kingName: str):
        self.king = kingName
        self.graph = defaultdict(list)
        self.deaths = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.deaths.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        visited = []
        self.dfs(visited,self.king)

        return visited
    
    def dfs(self , visited , node):
        if node not in self.deaths:
            visited.append(node)
        for child in self.graph[node]:
            self.dfs(visited,child)

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()