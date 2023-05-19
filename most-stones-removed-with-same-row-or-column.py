class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(u):
            if u==parent[u]:
                return u
            else:
                parent[u]=find(parent[u])
                return parent[u]
        def union(u,v):
            pu,pv=find(u),find(v)
            if pu==pv:
                return 
            if size[pv]>size[pu]:
                parent[pu]=pv
                size[pv]+=size[pu]
            else:
                parent[pv]=pu
                size[pu]+=size[pv]
        
        n=len(stones)
        mr=mc=0
        for i,j in stones:
            mr=max(mr,i)
            mc=max(mc,j)
        parent=[i for i in range(mr+mc+2)]
        size=[1 for i in range(mr+mc+2)]
        d={} 
        for i,j in stones:
            union(i,j+mr+1)
            d[i]=1
            d[j+mr+1]=1
        c=0 
        for i in d:
            if find(i)==i:
                c+=1 # counting the no. of components
        return n-c