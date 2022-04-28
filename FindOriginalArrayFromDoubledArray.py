class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        if len(changed)%2 or changed.count(0)%2:
            return []
        dic={changed[0]:[1,1]}
        for i in range(1,len(changed)):
            if not changed[i]/2 in dic and not changed[i] in dic:
                dic[changed[i]]=[1,1]
            elif changed[i]/2 in dic and not changed[i] in dic:
                if dic[changed[i]/2][0]==0:
                    dic[changed[i]]=[1,1]
                elif dic[changed[i]/2][0]>0:
                    y=dic[changed[i]/2][0]-1
                    dic[changed[i]/2]=[y,dic[changed[i]/2][1]]
            elif changed[i] in dic:
                if changed[i]/2==changed[i]:
                    if dic[changed[i]][0]==1:
                        dic[changed[i]]=[0,dic[changed[i]][1]] 
                    elif dic[changed[i]][0]==0:
                        dic[changed[i]]=[1,dic[changed[i]][1]+1]
                else:
                    x=dic[changed[i]][0]+1
                    c=dic[changed[i]][1]+1
                    dic[changed[i]]=[x,c]
        li=dic.keys()
        ans=[]
        for m in li:
            for n in range(dic[m][1]):
                if dic[m][0]==0:
                    ans.append(m)
        if len(ans)==len(changed)/2:return ans
        else:return []
                    
