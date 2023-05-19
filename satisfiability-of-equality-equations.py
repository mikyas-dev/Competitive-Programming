class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = {chr(i):chr(i) for i in range(97,123)}
        size = [1]*26

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x,y):
            parent_x = find(x)
            parent_y = find(y)
            if size[ord(parent_x)-97] < size[ord(parent_y)-97]:
                root[parent_x] = parent_y
                size[ord(parent_y)-97] += size[ord(parent_x)-97]
            else:
                root[parent_y] = parent_x
                size[ord(parent_x)-97] += size[ord(parent_y)-97]
            
        for eq in equations:
            if "==" in eq:
                union(eq[0],eq[3])
            
        for eq in equations:
            if "!=" in eq and find(eq[0]) == find(eq[3]):
                return False
        return True