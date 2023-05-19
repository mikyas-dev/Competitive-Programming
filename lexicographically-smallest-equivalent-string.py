class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = {chr(i):chr(i) for i in range(97,123)}
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(a,b):
            parent_x = find(a)
            parent_y = find(b)

            if parent_x > parent_y:
                root[parent_x] = parent_y
            else:
                root[parent_y] = parent_x
        
        for i in range(len(s1)):
            union(s1[i],s2[i])

        ans = ""
        for s in baseStr:
            parent_s = find(s)
            ans+=parent_s
        
        return ans